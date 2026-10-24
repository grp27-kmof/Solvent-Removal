# Solvent Removal

A Python-based tool for removing guest molecules and solvent components from Metal–Organic Framework (MOF) CIF structures using [`mofstructure`](https://github.com/bafgreat/mofstructure) and [ASE](https://wiki.fysik.dtu.dk/ase/).

The script supports **parallel processing** using Python's `ProcessPoolExecutor`, allowing multiple CIF files to be processed simultaneously.

## Features

- Processes multiple MOF CIF files in parallel.
- Removes guest molecules using `mofstructure`.
- Saves the cleaned structures as CIF files using ASE.

## Requirements

- Python 3.10 (recommended starting point; use a version compatible with the installed dependencies).
- Conda or Miniconda.
- MOF CIF input files.

## 1. Clone the Repository

```bash
git clone https://github.com/grp27-kmof/Solvent-Removal.git
cd Solvent-Removal
```

## 2. Create a Conda Environment


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

Create the directories from the repository root:

```bash
mkdir -p input output
```

Place your input `.cif` files inside the `input/` directory.

The script writes the processed files to `output/`. 

## 5. Configure the Input and Output Paths

Open `main.py` and update the following lines to match your system:

```python
input_dir = Path(r"/path/to/your/input")
output_dir = Path(r"/path/to/your/output")
```

## 6. Install Dependencies

Install the required Python packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 7. Configure Parallel Execution

The script uses Python's `ProcessPoolExecutor` to process several CIF files simultaneously.

In `main.py`, locate:

```python
MAX_WORKERS = 25
```

`MAX_WORKERS` specifies the maximum number of worker processes that can process CIF files concurrently.

This project was run on a **32-core workstation**, using 25 workers to perform parallel solvent removal.

You should adjust the number of workers according to the CPU cores and available RAM on your system.

## 8. Run the Script

After configuring the paths and worker count, execute:

```bash
python main.py
```

The script will:

1. Find all `.cif` files in the input directory.
2. Submit each CIF file to the process pool.
3. Load each structure using `mofstructure`.
4. Remove guest molecules.
5. Write the cleaned structure to the output directory.
6. Print the result or any processing error for each file.

Example terminal output:

```text
Found 1000 CIF files. Processing with 25 workers...

[MOF_001.cif] Saved: MOF_001.cif
[MOF_002.cif] Saved: MOF_002.cif
[MOF_003.cif] Saved: MOF_003.cif

All CIF files processed!
```

## Acknowledgements

This project uses:

- [`mofstructure`](https://github.com/bafgreat/mofstructure) for MOF structure handling and guest removal.
- [Atomic Simulation Environment (ASE)](https://wiki.fysik.dtu.dk/ase/) for reading and writing atomistic structures.
