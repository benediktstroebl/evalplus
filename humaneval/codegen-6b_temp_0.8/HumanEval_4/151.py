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
        raise ValueError('mean_absolute_deviation() requires at least 2 values')

    # The sum of the absolute differences from the mean: mean absolute deviation.
    mad = sum(abs(x - numbers[len(numbers)//2]) for x in numbers)

    # The square root of the number of data points: the number of standard
    # deviations from the mean.
    r = len(numbers) ** 0.5

    # The result.
    return r * mad/2

