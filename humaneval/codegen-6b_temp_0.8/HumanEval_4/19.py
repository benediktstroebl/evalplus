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
    # Mean of the numbers
    x_mean = sum(numbers) / float(len(numbers))
    # Use absolute value function to get absolute differences from
    # mean
    return sum([abs(num - x_mean) for num in numbers]) / len(numbers)
