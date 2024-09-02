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

    if not numbers:
        raise ValueError("List of input numbers cannot be empty.")

    if len(numbers) == 1:
        return 0.0

    sum_absolute_differences = sum(abs(number - mean(numbers)) for number in numbers)
    mean_absolute_deviation = sum_absolute_differences / len(numbers)
    return mean_absolute_deviation

