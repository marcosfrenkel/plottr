# plottr: modular data plotting and processing

A framework for inspecting data, based on flowcharts from *pyqtgraph*.
*plottr*'s main aim is to allow the user to define custom data processing flows and plotting.
A particular use case is data filtering and plotting.

## Quickstart

### Installation

In brief: clone the repo, and install using `pip install -e`

### inspectr: QCoDeS dataset inspection and (live) plotting

You can use the inspectr tool to get a simple overview over QCoDeS database
files, and plot datasets contained in the database.

To use: from within the plottr-directory, run `python apps/inspectr.py --dbpath <path to your .db file>`

For basic instructions, check out the Notebook *Live plotting qcodes data* under `/doc/examples`.

### Interactive usage

For now, check out the Notebook *Interactive data inspection* under `/doc/examples/`.

## Some notes on installing

Note: this package is not compatible with the original plottr tool. You might want to install freshly if you still use the old version.

### Requirements:
* python >= 3.6 (f-strings...)
* the usual: numpy, mpl, ...
* pandas >= 0.22
* xarray
* pyqtgraph >= 0.10.0

### python package

clone the repo, and install using `pip install -e plottr/`.

## Documentation

Docs are currently work in progress. You can find it here (still sparse, though!):
https://plottr.readthedocs.io

## If you're looking for the 'original' plottr package...

It's in the branch `plottr-original`


