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
    # Calculate mean of input numbers
    num_sum = sum(numbers)
    mean = num_sum / len(numbers)

    # Calculate squared differences from mean
    diffs = [x - mean for x in numbers]
    squared_diffs = [x**2 for x in diffs]

    # Calculate Mean Absolute Deviation
    mad = sum(squared_diffs) / len(numbers)

    return mad
