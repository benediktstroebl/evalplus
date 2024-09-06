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
    if not isinstance(numbers, List):
        raise TypeError("numbers must be a list")
    if len(numbers) < 2:
        raise ValueError("numbers must have at least 2 elements")

    numbers.sort()
    n = len(numbers)
    deviations = [abs(numbers[i] - numbers[i // 2]) for i in range(n)]
    return sum(deviations) / n

