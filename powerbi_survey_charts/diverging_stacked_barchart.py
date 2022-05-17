"""
===============================================================
Discrete distribution as diverging stacked horizontal bar chart
===============================================================

Diverging Stacked bar charts can be used to visualize Likert survey results.

This example visualizes the result of a survey in which people could rate
their agreement to questions on a five-element scale.

The horizontal stacking is achieved by calling `~.Axes.barh()` for each
category and passing the starting point as the cumulative sum of the
already drawn bars via the parameter ``left``.

The middle is calculated for each item so that the central Neutral value
is evenly balanced, with negative results on the left and positive on the right.
"""

import numpy as np
import matplotlib.pyplot as plt


def survey(results, category_names, middle_index=None, split_index=None):
    """
    Parameters
    ----------
    results : dict
        A mapping from question labels to a list of answers per category.
        It is assumed all lists contain the same number of entries and that
        it matches the length of *category_names*. The order is assumed
        to be from 'Strongly disagree' to 'Strongly aisagree'
    category_names : list of str
        The category labels.
    """

    # calculate limits
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    if split_index is not None:
        offsets = data[:, range(split_index)].sum(axis=1)
        lhs_max = max([sum(counts[:split_index]) for counts in results.values()])
        rhs_max = max([sum(counts[split_index:]) for counts in results.values()])
    else:
        middle_index = (data.shape[1] // 2) if middle_index is None else middle_index
        offsets = data[:, range(middle_index)].sum(axis=1) + data[:, middle_index] / 2

        lhs_max = max([sum(counts[:middle_index]) + counts[middle_index] / 2 for counts in results.values()])
        rhs_max = max([sum(counts[middle_index+1:]) + counts[middle_index] / 2 for counts in results.values()])
    lhs_max = lhs_max + (5 - lhs_max % 5) # round off to the nearest 5
    rhs_max = rhs_max + (5 - rhs_max % 5) # round off to the nearest 5

    # Color Mapping
    category_colors = plt.get_cmap('coolwarm_r')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot Bars
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths - offsets
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

    # Add Zero Reference Line
    ax.axvline(0, linestyle='--', color='black', alpha=.25)

    # X Axis
    ax.set_xlim(-lhs_max, rhs_max)
    ax.set_xticks(np.arange(-lhs_max, rhs_max + 1, 10))
    ax.xaxis.set_major_formatter(lambda x, pos: str(abs(int(x))))

    # Y Axis
    ax.invert_yaxis()

    # Remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Ledgend
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    # Set Background Color
    fig.set_facecolor('#FFFFFF')

    return fig, ax


def show_survey(results, category_names, middle_index=None, split_index=None):
    fig, ax = survey(results, category_names, middle_index=middle_index, split_index=split_index)
    plt.show()


def show_example():
    category_names = ['Strongly disagree', 'Disagree',
                      'Neither agree nor disagree', 'Agree', 'Strongly agree']
    results = {
        'Question 1': [10, 15, 17, 32, 26],
        'Question 2': [26, 22, 29, 10, 13],
        'Question 3': [35, 37, 7, 2, 19],
        'Question 4': [32, 11, 9, 15, 33],
        'Question 5': [21, 29, 5, 5, 40],
        'Question 6': [8, 19, 5, 30, 38]
    }

    show_survey(results, category_names)


if __name__ == '__main__':
    show_example()
