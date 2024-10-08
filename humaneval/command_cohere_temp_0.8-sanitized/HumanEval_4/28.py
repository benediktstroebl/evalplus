from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        raise ValueError("Input list is empty. Unable to calculate MAD.")

    mean = math.fmean(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)

    return mad