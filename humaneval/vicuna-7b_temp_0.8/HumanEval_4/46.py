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
    n = len(numbers)
    for i in range(n):
        x = numbers[i]
        x_mean = n / n
        x_deviation = abs(x - x_mean)
        total_deviation += x_deviation
    mean_deviation = total_deviation / (n - 1)
    return mean_deviation

