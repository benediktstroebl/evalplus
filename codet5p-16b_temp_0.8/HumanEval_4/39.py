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

    return sum(
        map(lambda x: abs(x - mean_absolute_deviation([numbers])), numbers)
    ) / len(numbers)
    # There is a simpler way to do it (without using map):
    # return statistics.mean(numbers) - statistics.median(numbers)
    # The problem is that map will return a list in order to calculate
    # statistics.median, and that will not work well for the deviation
    # calculation.
    # The other way is more elegant, but I've already implemented mean_absolute_deviation

