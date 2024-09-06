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
    sum_of_absolute_difference = 0
    sum_of_numbers = 0

    mean_numbers = sum(numbers) / len(numbers)
    for number in numbers:
        difference = abs(number - mean_numbers)
        sum_of_absolute_difference += difference
        sum_of_numbers += number

    return sum_of_absolute_difference / len(numbers)

