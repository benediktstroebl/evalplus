import math
import unittest
import numpy as np
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    numbers_sorted = sorted(numbers)
    mean = math.fsum(numbers_sorted) / len(numbers_sorted)
    mad = sum( abs(x - mean) for x in numbers_sorted) / len(numbers_sorted)
    return mad