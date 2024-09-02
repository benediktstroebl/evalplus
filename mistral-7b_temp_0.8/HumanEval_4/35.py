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
    assert isinstance(numbers, list), "input should be a list"
    assert all(isinstance(number, float) for number in numbers), "input should be a list of float"
    assert len(numbers) > 0, "input list should have at least one element"
    total_diff = 0
    avg = sum(numbers) / len(numbers)
    for number in numbers:
        total_diff += abs(number - avg)
    return total_diff / len(numbers)
