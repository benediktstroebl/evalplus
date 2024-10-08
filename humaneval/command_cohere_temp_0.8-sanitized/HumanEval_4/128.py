from typing import List
import numpy as np
import numpy.testing as nt
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]