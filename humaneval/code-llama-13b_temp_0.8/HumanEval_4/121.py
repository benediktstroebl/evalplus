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

    # START CHALLENGE SOLUTION

    # First, get the mean of numbers
    mean = sum(numbers) / len(numbers)

    # Now, calculate the average absolute distance between each value and the mean
    absolute_differences = []
    for n in numbers:
        absolute_differences.append(abs(n - mean))

    return sum(absolute_differences) / len(absolute_differences)

    # END CHALLENGE SOLUTION

