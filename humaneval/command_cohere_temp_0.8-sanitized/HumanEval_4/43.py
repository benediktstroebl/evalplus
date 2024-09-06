import numpy as np
import unittest
from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case).

    Parameters:
        numbers (list of float): List of numerical data.

    Returns:
        float: Mean Absolute Deviation value.
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))