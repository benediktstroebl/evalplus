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
    total_deviation = 0
    n = len(numbers)

    for i in range(1, n):
        for j in range(i + 1, n):
            deviation = abs(numbers[i] - numbers[j])
            total_deviation += deviation

    return total_deviation / (n - 1)

