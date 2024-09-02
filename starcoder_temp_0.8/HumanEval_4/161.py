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
    center_point = sum(numbers) / len(numbers)

    absolute_differences = [abs(n - center_point) for n in numbers]
    sum_absolute_differences = sum(absolute_differences)
    mean_absolute_deviation = sum_absolute_differences / len(numbers)

    return mean_absolute_deviation
