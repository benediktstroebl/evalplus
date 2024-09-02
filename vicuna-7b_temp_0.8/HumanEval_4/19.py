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
    total_deviation = 0.0
    for i in range(len(numbers)):
        absolute_deviation = abs(numbers[i] - numbers.mean())
        total_deviation += absolute_deviation
    return total_deviation / len(numbers)

