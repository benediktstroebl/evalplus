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
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    # Calculate mean deviation
    mean_deviation = [abs(mean - x) for x in numbers]
    # Calculate mean absolute deviation
    mean_absolute_deviation = sum(mean_deviation) / len(numbers)
    return mean_absolute_deviation

