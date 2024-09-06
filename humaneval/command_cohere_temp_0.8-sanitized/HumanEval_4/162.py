from typing import List
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
    if len(numbers) == 0:
        return 0.0  # Return 0 dev if an empty list is passed
    mean = math.fmean(numbers)  # Mean of the list
    deviation = sum(math.fabs(x - mean) for x in numbers) / len(numbers)  # Absolute deviation of each number
    return deviation