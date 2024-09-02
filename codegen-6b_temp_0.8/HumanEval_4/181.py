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
    # We expect numbers to be a list of floats
    # We can assume that list length is at least 1
    if not isinstance(numbers, list):
        raise TypeError("Expected list of numbers")
    if len(numbers) < 1:
        raise ValueError("List of numbers must be at least 1")
    if not all(isinstance(x, float) for x in numbers):
        raise TypeError("List must only contain floats")
    # return abs(numbers - mean(numbers))
    return sum(abs(x - mean(numbers)) for x in numbers) / len(numbers)

