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

    length = len(numbers)
    if length < 2:
        return 0.0

    # Mean of the dataset
    mean = sum(numbers) / length

    # Sum of the absolute deviations from the mean:
    # deviations = [abs(n - mean) for n in numbers]

    # Calculate the mean of the deviations:
    # mean_deviation = sum(deviations) / length

    # Calculate the mean absolute deviation:
    mad = sum(abs(n - mean) for n in numbers) / length

    return mad

