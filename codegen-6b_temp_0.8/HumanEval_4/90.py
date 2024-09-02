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
    # Calculate mean absolute deviation for this data
    n = len(numbers)
    # Median is central value, so remove one more than the number of items
    # in the list
    median = float(numbers[int((n - 1) / 2)])
    # Ignore any negative numbers
    ma_devs = list(map(lambda x: abs(x - median), numbers))
    return sum(ma_devs) / n

