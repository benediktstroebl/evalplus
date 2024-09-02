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
    if len(numbers) < 3:
        raise ValueError('Minimum 3 elements needed')
    sorted_list = sorted(numbers)
    n = len(numbers)
    deviations = 0.0
    for i in range(1, n):
        deviations += abs(sorted_list[i] - sorted_list[i-1])
    return deviations / float(n-1)
