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
    num_values = len(numbers)
    if num_values == 0:
        return 0.0

    num_mean = sum(numbers) / num_values
    dev = [abs(x - num_mean) for x in numbers]
    return sum(dev) / num_values

