from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate the Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset:
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the input list
    """
    return math.sqrt(sum((x-mean(numbers))**2 for x in numbers) / len(numbers))
def mean(numbers: List[float]) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(numbers)/len(numbers)