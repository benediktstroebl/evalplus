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
    # make sure numbers is an iterable
    if not isinstance(numbers, list):
        raise TypeError(f"Expected a list but got {type(numbers)}")
    # make sure all numbers within numbers are floats
    if not all(isinstance(number, float) for number in numbers):
        raise TypeError(f"All elements must be floats")
    # make sure there is at least one number in the list
    if len(numbers) < 1:
        raise ValueError(f"Expected a non-empty list")

    mean = sum(numbers) / len(numbers)
    mad = 0
    for number in numbers:
        mad += abs(number - mean)
    return mad / len(numbers)

