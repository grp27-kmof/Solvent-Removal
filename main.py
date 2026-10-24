import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

from mofstructure import structure
from ase.io import write

input_dir = Path(r"/home/ubuntu/Desktop/MOF_Anode_27/Solvent/input")
output_dir = Path(r"/home/ubuntu/Desktop/MOF_Anode_27/Solvent/output")

MAX_WORKERS = 25


def process_cif(input_file: Path, output_dir: Path) -> str:
    """
    Worker function: processes a single CIF file.
    Must be top-level (importable) so it can be pickled for multiprocessing on Windows.
    """
    try:
        output_file = output_dir / f"{input_file.stem}.cif"

        mof = structure.MOFstructure(filename=str(input_file))

        clean_structure = mof.remove_guest()

        write(str(output_file), clean_structure)

        return f"Saved: {output_file.name}"
    except Exception as e:
        return f"Error processing {input_file.name}: {e}"


def main():
    output_dir.mkdir(parents=True, exist_ok=True)

    cif_files = sorted(input_dir.glob("*.cif"))
    if not cif_files:
        print("No CIF files found.")
        return

    print(f"Found {len(cif_files)} CIF files. Processing with {MAX_WORKERS} workers...\n")

    with ProcessPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(process_cif, f, output_dir): f
            for f in cif_files
        }

        for future in as_completed(futures):
            input_file = futures[future]
            try:
                result = future.result()
                print(f"[{input_file.name}] {result}")
            except Exception as e:
                print(f"[{input_file.name}] Unhandled error: {e}")

    print("\nAll CIF files processed!")


if __name__ == "__main__":
    main()