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
    mean = sum(numbers) / len(numbers)
    numbers = numbers[::-1]  # move numbers to right side
    x_mean = mean
    i = 0
    while i < len(numbers) - 1:
        current_x = numbers[i]
        abs_diff = abs(current_x - x_mean)
        deviation = abs_diff / x_mean
        i += 1
        numbers = numbers[i:]
        if len(numbers) % 2 == 0:
            deviation = deviation + deviation
        else:
            deviation = deviation / 2
    return deviation