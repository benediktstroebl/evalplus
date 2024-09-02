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

    assert numbers, "Given list of numbers cannot be empty."

    numbers_sum = sum(numbers)
    numbers_mean = numbers_sum / len(numbers)
    numbers_mean_deviation = [abs(x - numbers_mean) for x in numbers]
    return sum(numbers_mean_deviation) / len(numbers_mean_deviation)
    
