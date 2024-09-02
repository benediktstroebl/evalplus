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
    n = len(numbers)
    if n == 0:
        return 0
    # If there is only one number in the list, just return 0 for the MAD
    # This is to avoid a divide by 0 error
    if n == 1:
        return 0
    total = sum(numbers)
    average = total / n
    absolute_differences = [abs(x - average) for x in numbers]
    return sum(sorted(absolute_differences)) / (n - 1)

