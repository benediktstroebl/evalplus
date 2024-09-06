from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # List comprehension to calculate absolute deviations from the mean
    abs_deviations = [abs(num - sum(numbers) / len(numbers)) for num in numbers]
    # Returning the mean of absolute deviations
    return float(sum(abs_deviations) / len(abs_deviations))