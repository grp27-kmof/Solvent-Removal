# Solvent Removal

A Python-based tool for removing guest molecules and solvent components from Metal–Organic Framework (MOF) CIF structures using [`mofstructure`](https://github.com/bafgreat/mofstructure) and [ASE](https://wiki.fysik.dtu.dk/ase/).

The script supports **parallel processing** using Python's `ProcessPoolExecutor`, allowing multiple CIF files to be processed simultaneously.

## Features

- Processes multiple MOF CIF files in parallel.
- Removes guest molecules using `mofstructure`.
- Saves the cleaned structures as CIF files using ASE.
- Allows the number of parallel workers to be configured.

## Requirements

- Python 3.10
- Conda or Miniconda.
- MOF CIF input files.

## 1. Clone the Repository

```bash
git clone https://github.com/grp27-kmof/Solvent-Removal.git
cd Solvent-Removal
```

## 2. Create a Conda Environment

Create a dedicated Conda environment for the project:

```bash
conda create -n kmof-solvent python=3.10 -y
```

## 3. Activate the Environment

```bash
conda activate kmof-solvent
```

Make sure the environment is activated before installing dependencies or running the script.

## 4. Create Input and Output Directories

Create two directories for the CIF files:

- `input/` — contains the original MOF CIF files.
- `output/` — stores the solvent-removed CIF files.

Run the following command from the repository root:

```bash
mkdir -p input output
```

Place your input `.cif` files inside the `input/` directory.

The script saves the processed files to the `output/` directory.

## 5. Configure Input and Output Paths

Open `main.py` and update the paths to match your system:

```python
input_dir = Path(r"/path/to/your/input")
output_dir = Path(r"/path/to/your/output")
```

**Important:** Ensure that `input_dir` points to the directory containing your CIF files and `output_dir` points to the desired output location.

## 6. Install Dependencies

Install the required Python packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 7. Configure Parallel Execution

The script uses Python's `ProcessPoolExecutor` to process multiple CIF files concurrently.

In `main.py`, locate:

```python
MAX_WORKERS = 25
```

`MAX_WORKERS` specifies the maximum number of worker processes that can run concurrently. The actual number of active workers is also limited by the number of available CIF files.

This project was run on a **32-core workstation using 25 workers**.

Adjust the worker count according to your system's CPU resources and available RAM. More workers do not always result in faster execution, particularly when memory usage becomes a bottleneck.

## 8. Run the Script

After configuring the paths and worker count, run:

```bash
python main.py
```

The script will:

1. Find all `.cif` files directly inside the input directory.
2. Submit the files to the process pool.
3. Load each structure using `mofstructure`.
4. Remove guest molecules.
5. Write the cleaned structure to the output directory.
6. Print the result or any processing error for each file.

Example terminal output (illustrative):

```text
Found 1000 CIF files. Processing with 25 workers...

[MOF_001.cif] Saved: MOF_001.cif
[MOF_002.cif] Saved: MOF_002.cif
[MOF_003.cif] Saved: MOF_003.cif

All CIF files processed!
```

The number of CIF files and worker processes will depend on your input and configuration.

**Note:** The final completion message does not guarantee that every CIF file was processed successfully. Check the per-file messages for errors.

## 9. Input and Output Structure

Example input directory:

```text
input/
├── MOF_001.cif
├── MOF_002.cif
└── MOF_003.cif
```

Example output directory:

```text
output/
├── MOF_001.cif
├── MOF_002.cif
└── MOF_003.cif
```

Output filenames retain the corresponding input filenames. Existing output files with matching names may be overwritten.

## Acknowledgements

This project uses:

- [`mofstructure`](https://github.com/bafgreat/mofstructure) for MOF structure handling and guest removal.
- [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/) for writing atomistic structures.
