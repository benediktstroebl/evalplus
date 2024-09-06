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

    # Calculate the sum of all the numbers
    n = len(numbers)
    sum_of_numbers = numbers[0]
    for number in numbers:
        sum_of_numbers += number

    # Calculate the mean of the numbers
    sum_of_numbers = sum_of_numbers / n
    mean = numbers[0]

    # Calculate the sum of the absolute differences
    sum_of_abs_diff = sum([abs(x - mean) for x in numbers])

    # Calculate the mean absolute deviation
    return sum_of_abs_diff / n

