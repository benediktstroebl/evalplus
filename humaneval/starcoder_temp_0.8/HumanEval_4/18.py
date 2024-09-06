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
    # calculate the mean of all numbers
    mean = sum(numbers) / len(numbers)
    # calculate the absolute differences between all numbers and the mean
    absolute_differences = [abs(number - mean) for number in numbers]
    # calculate the mean of the absolute differences
    return sum(absolute_differences) / len(numbers)

