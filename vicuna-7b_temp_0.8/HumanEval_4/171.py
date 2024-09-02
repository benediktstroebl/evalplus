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
    n = len(numbers)
    sum_of_absolute_deviations = 0
    for i in range(n):
        number = numbers[i]
        absolute_deviation = abs(number - numbers.mean())
        sum_of_absolute_deviations += absolute_deviation
    return sum_of_absolute_deviations / n

