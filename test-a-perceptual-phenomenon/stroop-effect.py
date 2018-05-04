import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.stats import ttest_rel
from scipy.stats import t


def show_stats(data, heading, unit):
    """
    This function displays the mean, median, standard deviation of sample.
    Params
    data: The data to work on. (1D numpy array)
    heading: The heading of the data
    unit: unit in which data is represented
    """
    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data, ddof=1)

    print(heading)
    print('Mean(' + unit + ')\t', 'Median(' + unit + ')\t', 'Std(' + unit + ')')
    print(mean, '\t', median, '\t', std)


def visualize_hist(data1, data2, labels, legend_title, legends, savefig=True, show_mean=True):
    """
    This function visualizes the two datasets
    Params
    data1: 1D numpy array of first dataset
    data2: 1D numpy array of second dataset
    labels: list of x label and y label
    legend_title: Title of legends
    legends: list of 2 legends
    savefig: if true save figure as png file
    """
    # Visualize data
    plt.figure(0)
    # labels
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    # Data to histogram
    plt.hist(incong, color='green')
    plt.hist(cong, color='red')
    # Show mean
    if show_mean:
        plt.axvline(cong.mean(), color='blue', linestyle='dashed', linewidth=2)
        plt.axvline(incong.mean(), color='cyan', linestyle='dashed', linewidth=2)
    # Legends
    green_patch = mpatches.Patch(color='green', label=legends[1])
    red_patch = mpatches.Patch(color='red', label=legends[0])
    plt.legend(title=legend_title, handles=[red_patch, green_patch])
    # Save Visualization
    if savefig:
        plt.savefig('visualize.png', bbox_inches='tight')
    # Show
    plt.show()


def visualize_box(data1, data2, labels, savefig=True, show_mean=True):
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    bp = ax.boxplot([data1, data2])
    ax.set_xticklabels(labels)
    if savefig:
        plt.savefig('box_visualize.png', bbox_inches='tight')
    plt.show()


def perform_ttest(data1, data2):
    """
    Performs t-test on related samples
    params:
    data1: 1D sample 1 numpy array
    data2: 1D sample 2 numpy array
    """
    md = np.mean(data1) - np.mean(data2)
    sem = np.sqrt(np.std(data1, ddof=1)+np.std(data1, ddof=1))
    df = data1.shape[0] - 1
    t_critical = t.isf([0.025], [[df]])[0][0]
    moe = t_critical * sem
    
    print(' t-critical value: ', t_critical)
    print(' Mean Difference: ', md)
    print(' Standar Error = %6.3f df = %d' % (sem, df))
    print(' t-statistic = %6.3f pvalue = %f' % ttest_rel(data1, data2))
    print(' CI: (%6.4f, %6.4f)' % (md - moe, md + moe))


# Read in data
df = pd.read_csv('stroop-effect-data.csv')
cong = np.asarray(df['Congruent'])
incong = np.asarray(df['Incongruent'])

# Display Descriptive stats
print()
show_stats(cong, 'Congruent', 'time')
print()
show_stats(incong, 'Incongruent', 'time')

# Visualize plot
visualize_hist(incong, cong, ['time', 'count'], 'Congruency', ['Congruent', 'Incongruent'])
visualize_box(cong, incong, ['Congruent', 'Incongruent'])
print('\n Generated Histogram & Box Plot')
perform_ttest(cong, incong)
