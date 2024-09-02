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
    # We make sure that all numbers are of the same type so we can work with
    # them consistently throughout the algorithm
    for number in numbers:
        assert isinstance(number, float)
    total = 0.0
    for number in numbers:
        total += abs(number - mean(numbers))
    return total / len(numbers)

