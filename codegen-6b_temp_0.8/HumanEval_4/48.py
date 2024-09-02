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
    assert len(numbers) > 1, "Mean Absolute Deviation requires at least two elements."

    mean_ = float(sum(numbers)) / len(numbers)
    def absolute_deviation(num):
        return abs(num - mean_)

    absolute_deviations = map(absolute_deviation, numbers)
    return float(sum(absolute_deviations)) / len(absolute_deviations)

