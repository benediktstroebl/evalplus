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
    # First, move the point closer to the mean
    # Thus, the value of the average is closer to the mean
    # If we calculated the MAD for a list of points,
    # the larger the points would be from the mean,
    # the smaller the MAD would be.
    numbers_mean = sum(numbers) / len(numbers)

    numbers_subtracted = [abs(n - numbers_mean) for n in numbers]
    return sum(numbers_subtracted) / len(numbers_subtracted)

