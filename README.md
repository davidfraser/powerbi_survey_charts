PowerBI Survey Charts
=====================

This package contains matplotlib charting methods useful for PowerBI display of survey results

This includes using diverging stacked bar charts to display results from surveys using the Likert scale.

The [Likert scale](https://en.wikipedia.org/wiki/Likert_scale) is a familiar psychometric scale in surveys,
indicating a range of agreement/disagreement with statements.

A good account of why Diverging Stacked Bar Charts are a useful way to display this data is found at
_[Diverging Bars, Why & How](https://towardsdatascience.com/diverging-bars-why-how-3e3ecc066dce)_ by Darío Weitz.

API
---

The `powerbi_survey_charts` package contains two modules, `diverging_stacked_barchart` and `horizontal_barchart_distribution`.
The latter is slightly modified from one of the standard matplotlib examples.
The former is a version of that adapted to display Diverging Stacked Bar Charts.

Both modules contain three methods:
- `survey(results, category_names, ...)` returns a matplotlib figure and axis containing a chart of the given data
- `show_survey(results, category_names, ...)` takes that same survey and displays it
- `show_example()` displays the survey with some included sample data, to make it easier to quickly test

The code of `show_example` is instructive for how to use the modules:
- `results` is a dictionary mapping question titles to counts of different responses on the Likert scale (this can take any number of inputs).
- `category_names` is a list of the labels for the Likert scale responses (e.g. `["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]`).

Usage in Power BI Desktop
-------------------------

To use this in Power BI Desktop, you need to follow the general technique to [Create Power BI visuals by using Python](https://docs.microsoft.com/en-us/power-bi/connect-data/desktop-python-visuals).
Ensure that this package is included in the Python environment Power BI is using.
Get the data into the shape required as described above.
Then calling `show_survey(results, category_names)` should result in the chart being displayed in PowerBI.

Note that there are additional requirements for this to work in Power BI online.

Credits
-------
The original sample code was taken from the matplotlib examples and modifications of it on StackOverflow by [Eitan Lees](https://stackoverflow.com/users/3320620/eitanlees). See:
* [examples/lines_bars_and_markers/horizontal_barchart_distribution.py](https://github.com/matplotlib/matplotlib/blob/main/examples/lines_bars_and_markers/horizontal_barchart_distribution.py)
* [Create a Diverging Stacked Bar Chart in matplotlib](https://stackoverflow.com/a/69976552/120398)

License
-------

This is released under the Python Software Foundation License, 2.0 (the same as the Matplotlib sample code on which it was based)
