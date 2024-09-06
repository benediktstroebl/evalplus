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
    # Explicitly casting to float to avoid issues with integers
    mean = float(np.mean(numbers))
    deviance = np.abs(np.array(numbers) - mean)
    return np.mean(deviance)