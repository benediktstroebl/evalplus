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
    x_mean = sum(numbers) / len(numbers)
    absolute_difference = []
    for x in numbers:
        absolute_difference.append(abs(x - x_mean))
    return sum(absolute_difference) / len(absolute_difference)

