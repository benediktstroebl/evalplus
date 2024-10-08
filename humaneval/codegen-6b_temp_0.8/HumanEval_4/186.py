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
    # Mean
    # NOTE: we expect numbers to be a list of floats (not "complex" as per the
    #       question's instructions)
    mean = sum(numbers) / len(numbers)
    # Mean absolute difference between each element and the mean of
    # everything
    abs_diff = [abs(n - mean) for n in numbers]
    return sum(abs_diff) / len(abs_diff)

