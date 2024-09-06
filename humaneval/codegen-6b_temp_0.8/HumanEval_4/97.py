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
    if len(numbers) == 0:
        raise ValueError('Empty list')

    # Calculate mean.
    mean = sum(numbers) / len(numbers)

    abs_dev = [abs(x - mean) for x in numbers]
    average_abs_dev = sum(abs_dev) / len(numbers)

    return average_abs_dev

