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

    # Calculate mean of numbers
    nums_sum = sum(numbers)
    mean = nums_sum / len(numbers)

    # Initialize MAD
    MAD = 0.0

    # Calculate MAD for each number
    for i, num in enumerate(numbers):
        abs_diff = abs(num - mean)
        MAD += abs_diff / len(numbers)

    return MAD

