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
    if not numbers:
        raise ValueError("You have to provide at least one number")
    try:
        mean = sum(numbers) / float(len(numbers))
    except TypeError:
        raise TypeError("You have to pass a list of numbers")
    if len(numbers) == 1:
        return 0
    return sum(abs(x - mean) for x in numbers) / float(len(numbers))

