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
    if len(numbers) == 0:
        return 0.0

    n = len(numbers)
    sum_of_abs_diffs = 0.0
    for i in range(1, n):
        number = numbers[i]
        abs_diff = abs(numbers[i - 1] - number)
        sum_of_abs_diffs += abs_diff
        average_abs_diff = sum_of_abs_diffs / (i - 1)
        mean_diff = numbers[i - 1] - number
        average_mean_diff = mean_diff / (i - 1)
        sum_of_abs_diffs -= average_mean_diff * abs_diff
    return sum_of_abs_diffs / n

