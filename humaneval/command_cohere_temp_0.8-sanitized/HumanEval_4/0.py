from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if len(numbers) == 0:
        return 0.0  # Return 0 if the input list is empty
    mean = math.fmean(numbers)  # Calculate the mean of the list
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)  # Calculate the sum of absolute deviations
    return mad