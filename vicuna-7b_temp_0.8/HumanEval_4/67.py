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
        return 0.0

    numbers_sorted = sorted(numbers)
    mean = sum(numbers) / len(numbers)
    x_mean = numbers_sorted[0]
    x_mean_squared = sum([x**2 for x in numbers_sorted]) / len(numbers_sorted)

    for i in range(1, len(numbers_sorted)):
        x = numbers_sorted[i]
        delta = x - x_mean
        x_mean_squared -= delta**2
        x_mean = x
    return x_mean_squared / (len(numbers_sorted) - 1)

