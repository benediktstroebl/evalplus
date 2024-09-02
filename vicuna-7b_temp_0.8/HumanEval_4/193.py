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
    median = median_of_sorted(numbers)  # calculate the median of the numbers
    mean = sum(numbers) / len(numbers)  # calculate the mean of the numbers
    n = len(numbers)
    devs = [abs(numbers[i] - mean) for i in range(n)]
    return sum(devs) / n

