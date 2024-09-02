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
    mean = sum(numbers) / len(numbers)
    variance = 0.0
    squared_deviation: List[float] = []
    for x in numbers:
        squared_deviation.append(x - mean) ** 2
        variance += squared_deviation[-1]
        squared_deviation.pop()
    variance = sum(variance)
    return (sum(abs(squared_deviation)) / len(numbers)) ** 0.5

