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
    sum_of_numbers = sum(numbers)
    number_of_numbers = len(numbers)
    mean_of_numbers = sum_of_numbers / number_of_numbers
    number_deviations = 0.0

    for number in numbers:
        number_deviations += abs(number - mean_of_numbers)

    return number_deviations / number_of_numbers

