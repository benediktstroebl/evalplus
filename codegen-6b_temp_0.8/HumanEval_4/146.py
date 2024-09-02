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
    if n == 0:
        # no numbers, mean absolute deviation is 0
        return 0
    if n == 1:
        # one element, mean absolute deviation is the difference between the
        # element and the mean:
        return abs(numbers[0] - float(numbers[0]).__round__())
    m = sum(numbers) / n  # mean
    return sum([abs(x - m) for x in numbers]) / n

