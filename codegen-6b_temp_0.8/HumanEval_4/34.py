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
    if len(numbers) < 2:
        msg = "Must have at least 2 elements to calculate Mean Absolute Deviation."
        raise ValueError(msg)
    sum_of_abs_deviations = 0.0
    for i, value in enumerate(numbers, 1):
        sum_of_abs_deviations += abs(value - numbers[0])
    mean_value = sum_of_abs_deviations / i
    return mean_value

