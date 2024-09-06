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
    # Silently handle empty input, return NaN for undefined MAE
    if not numbers:
        return np.nan
    
    # handle single value input, return 0 for such cases
    if len(numbers) == 1:
        return 0.0
    
    # Compute mean
    mean = np.mean(numbers)
    
    # Compute absolute deviations from the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Return the mean of the absolute deviations
    return np.mean(absolute_deviations)
numbers = [1.0, 2.0, 3.0, 4.0]