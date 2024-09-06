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
    assert all(isinstance(n, (float, int)) for n in numbers)

    sum_deviation = 0
    for number in numbers:
        sum_deviation += abs(number - sum(numbers) / len(numbers))
    return sum_deviation / len(numbers)

