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
    sum_of_absolute_differences = sum([abs(x - sum(numbers)) for x in numbers])
    sum_of_squared_differences = sum([(x - sum(numbers))**2 for x in numbers])
    return sum_of_absolute_differences / len(numbers)