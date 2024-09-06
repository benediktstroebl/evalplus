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

    # mean
    sum_of_numbers = sum(numbers)
    mean = sum_of_numbers / len(numbers)

    # abs_diff
    absolute_diff = [abs(x - mean) for x in numbers]
    # Note: we are not using 'for' here to make it easier for you to understand
    # the logic

    # average_diff
    # Note: you can use a one-liner to calculate this
    average_diff = sum(absolute_diff) / len(numbers)

    return average_diff

