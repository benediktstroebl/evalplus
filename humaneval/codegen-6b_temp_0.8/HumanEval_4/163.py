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
        raise ValueError("Empty input")
    if not isinstance(numbers, list):
        raise ValueError("Input not a list")
    result = 0.0
    total_element_count = len(numbers)
    for number in numbers:
        result += abs(number - sum(numbers) / total_element_count)
    return result / total_element_count

