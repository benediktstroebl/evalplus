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
    # Calculate the mean of the numbers
    mean = float(sum(numbers)) / len(numbers)

    # Calculate the absolute difference from each number to the mean
    deviations = [abs(numbers[i] - mean) for i in range(len(numbers))]

    # Calculate the sum of the absolute differences
    sum_deviations = sum(deviations)

    # Calculate the variance of the absolute differences
    variance = float(sum((deviations ** 2) * (len(deviations) - 1)))

    # Calculate the standard deviation
    std = variance ** 0.5

    # Calculate the mean absolute deviation
    mad = (sum_deviations / len(numbers)) / std

    return mad

