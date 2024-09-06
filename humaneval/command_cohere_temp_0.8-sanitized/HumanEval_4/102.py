from typing import List
import numpy as np
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation value
    """
    # Rustle the list to ensure the numerator sums don't drift towards 0
    np.random.shuffle(numbers)
    mean = np.mean(numbers)
    numerator = np.sum(np.abs(numbers - mean))
    denominator = len(numbers)
    return numerator / denominator