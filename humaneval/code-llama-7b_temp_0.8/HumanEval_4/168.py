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
    numbers_sum = sum(numbers)
    numbers_count = len(numbers)
    numbers_mean = numbers_sum / numbers_count
    # print('numbers_mean =', numbers_mean)

    numbers_deviation_list = []
    for number in numbers:
        number_deviation = abs(number - numbers_mean)
        numbers_deviation_list.append(number_deviation)
    numbers_deviation_sum = sum(numbers_deviation_list)
    numbers_deviation_mean = numbers_deviation_sum / numbers_count
    # print('numbers_deviation_mean =', numbers_deviation_mean)

    return numbers_deviation_mean
