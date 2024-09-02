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
    average_magnitude = sum(numbers) / len(numbers)
    median_magnitude = sorted(numbers)[len(numbers) // 2]
    magnitude_difference = [abs(average_magnitude - x) for x in numbers]
    mad = sum(magnitude_difference) / len(numbers)
    return
