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
    # If the mean is 0, the MAD is 0
    if numbers == []:
        return 0
    # Check for negatives here, because we need to avoid pow(negative, 1/2)
    numbers = [num for num in numbers if num > 0]
    if len(numbers) <= 1:
        return 0

    return sum(abs(num - numbers[len(numbers) // 2]) for num in numbers) / len(numbers)

