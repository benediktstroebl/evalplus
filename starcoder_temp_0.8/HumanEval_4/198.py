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
    # The mean of the dataset
    mean = sum(numbers) / len(numbers)

    # The sum of all the absolute differences between each element
    # and the mean
    deviation_sum = 0
    for number in numbers:
        deviation_sum += abs(mean - number)

    # The average deviation of all the elements
    return deviation_sum / len(numbers)
