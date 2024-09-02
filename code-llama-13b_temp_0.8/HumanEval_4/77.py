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
    n = len(numbers)
    numbers_sum = 0
    for number in numbers:
        numbers_sum += number
    average = numbers_sum / n
    numbers_deviation = []
    for number in numbers:
        numbers_deviation.append(abs(number - average))
    numbers_deviation_sum = 0
    for number in numbers_deviation:
        numbers_deviation_sum += number
    return numbers_deviation_sum / n

