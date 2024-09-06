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
    # Calculate mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate absolute difference between each element and mean of this dataset
    diffs = [abs(mean - x) for x in numbers]

    # Calculate mean of absolute difference between each element and mean of this dataset
    return sum(diffs) / len(diffs)

