from typing import List
import numpy as np
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the list
    """
    # Ensure the list has numeric values only
    if not np.all(np.array(numbers) >= 0):
        raise ValueError("Input list should only contain positive numeric values.")
    
    return math.fsum(np.abs(np.array(numbers) - np.mean(np.array(numbers)))) / len(numbers)