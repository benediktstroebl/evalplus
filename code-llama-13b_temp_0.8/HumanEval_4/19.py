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
    numbers_mean = sum(numbers) / len(numbers)
    deviation_values = []
    for number in numbers:
        deviation = abs(number - numbers_mean)
        deviation_values.append(deviation)

    return sum(deviation_values) / len(deviation_values)

