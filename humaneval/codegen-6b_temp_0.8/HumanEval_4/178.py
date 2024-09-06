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
    # calculate the mean:
    mean = sum(numbers) / len(numbers)
    # store the absolute difference abs(x - mean) for each element x
    absolute_difference = [abs(x - mean) for x in numbers]
    # return the mean of absolute difference
    return sum(absolute_difference) / len(absolute_difference)

