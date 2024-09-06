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
    assert len(numbers) > 0
    assert len(numbers) == len(set(numbers))

    # How many number are there in this set?
    len_numbers = len(numbers)

    # Calculate mean and center point
    mean = sum(numbers) / len_numbers
    centerpoint = sum([abs(num - mean) for num in numbers]) / len_numbers

    return centerpoint

