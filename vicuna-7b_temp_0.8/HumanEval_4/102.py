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
    # First, calculate the mean of the numbers
    mean = float(sum(numbers) / len(numbers))

    # Then, calculate the MAD by taking the absolute difference of each number from the mean
    # and square each difference, then sum them up.
    MAD = sum([abs(numbers[i] - mean) ** 2 for i in range(len(numbers))]) / len(numbers)

    return MAD