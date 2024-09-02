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
    assert len(numbers) > 0, "Input list of numbers cannot be empty."
    mean_of_numbers = sum(numbers) / len(numbers)
    sum_of_squared_differences = 0
    for number in numbers:
        sum_of_squared_differences += (number - mean_of_numbers)**2

    return (sum_of_squared_differences / len(numbers))**0.5

