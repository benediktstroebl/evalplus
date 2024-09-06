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
    # if len(numbers) == 0:
    #     raise ValueError("This function requires a non-empty input list.")
    # calculate mean of the dataset
    nums_mean = sum(numbers) / len(numbers)
    # calculate mean absolute deviation
    mad = 0.0
    for num in numbers:
        abs_diff = abs(num - nums_mean)
        mad += abs_diff
    return mad

