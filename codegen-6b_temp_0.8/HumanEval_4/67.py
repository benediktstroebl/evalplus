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
    n = len(numbers)
    # calculate the mean of the list
    x_mean = sum(numbers) / n
    # calculate the absolute differences from the mean
    abs_diff = map(lambda x: abs(x - x_mean), numbers)
    # calculate the new MAD
    mad = (sum(abs_diff) / n) ** 0.5
    return mad

