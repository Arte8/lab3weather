Weather summary lab3

This project downloads Toronto hourly weather data from Open-Meteo, validates each reading, calculates statistics, and saves a JSON summary.

Open Anaconda Prompt in the repository folder:
clone into new folder (git clone https://github.com/ARTE8/lab3weather.git weather-summary-review)
(cd weather-summary-review)
(conda env create -n weather-summary-review -f environment.yml)
(conda activate weather-summary-review)
(python -m pip install -e .)
(python main.py)

```

The editable installation allows importing `weathersummary` without
changing `sys.path`.


Internet access is required for downloading weather data.
The output is saved to `data/processed/summary.json`.

At least 50 downloaded records and 50 valid readings are required.
Download failures print a clear message and exit without a traceback.

With the environment activated, run:

```cmd
python -m unittest discover -s tests
```

The tests use hand-made records and do not access the network.
They check numeric conversion, rejection of invalid values, and the record's string representation.


- `config.py`: source URL, request timeout, and relative output path. - `models.py`: `WeatherReading`, which validates values in `__init__`. - `sources.py`: `WeatherSource`, which returns reading objects and counts.
  This is the only module importing `requests`.
- `processing.py`: constructs readings and counts rejected records.
- `aggregations.py`: the `Aggregation` base class and subclasses.
- `report.py`: builds the summary and writes JSON.
- `__init__.py`: re-exports the public classes and functions.
- `main.py`: connects the components and prints results or errors.


`WeatherReading` represents one hourly record and defines `__str__`.
`WeatherSource` handles retrieval. Both have an explicit `__init__`
method and a class docstring.

`OverallStatistics`, `DailyStatistics`, and `UniqueDates` inherit from
`Aggregation` and override `compute()`.

The summary builder loops over aggregation objects and calls their `compute()` methods without checking their subclasses.


`environment.yml` specifies the Conda environment, Python, and pip.
`requirements.txt` pins requests, pandas, and NumPy.
`pyproject.toml` declares the package dependencies and src layout.


The refactor retains the original summary keys, validation rules,
statistics, and minimum-record checks.

To verify equivalent results, run both versions using the same saved
API response and compare the parsed JSON summaries. Separate live
downloads may contain different weather data.


enjoy
and give Art good grades!
