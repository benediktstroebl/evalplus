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
    if len(numbers) < 2:
        raise ValueError("Not enough numbers (minimum 2)")
    sorted_numbers = sorted(numbers)
    m = len(sorted_numbers) // 2
    return sum([abs(sorted_numbers[i] - sorted_numbers[m]) for i in (m - 1, m)]) / (2 * (len(sorted_numbers) - 1))

