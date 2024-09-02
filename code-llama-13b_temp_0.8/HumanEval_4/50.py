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
    # below line is needed to prevent StopIteration error when calling next()
    if len(numbers) == 0:
        return 0.0

    numbers_sum = 0
    numbers_len = 0
    for number in numbers:
        numbers_sum += number
        numbers_len += 1
    mean = numbers_sum / numbers_len

    mad_sum = 0
    for number in numbers:
        mad_sum += abs(mean - number)
    return mad_sum / numbers_len

