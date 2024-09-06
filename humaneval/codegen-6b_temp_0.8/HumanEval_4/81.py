from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # get median
    from numpy import median

    median_val = median(numbers)
    # print(f'median_val: {median_val}')
    # get the absolute difference against the median
    abs_dev = abs(numbers - median_val)
    # print(f'abs_dev: {abs_dev}')
    # make an array of them, then get the mean
    abs_dev = abs_dev.tolist()
    mad = sum(abs_dev) / len(abs_dev)
    midpoint = mad / 2
    # print(f'midpoint: {midpoint}')
    # use the formula to calculate the MAD
    mad = (abs_dev[0] - midpoint) + (abs_dev[len(abs_dev) - 1] - midpoint)
    return round(mad, 2)

