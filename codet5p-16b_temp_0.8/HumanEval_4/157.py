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
        raise ValueError("Input list must not be empty!")
    number_sum = sum(numbers)
    mean_of_numbers = number_sum / len(numbers)
    mad = sum([abs(number - mean_of_numbers) for number in numbers]) / len(numbers)
    return mad
