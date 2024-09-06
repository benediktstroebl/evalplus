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
    assert numbers and all(isinstance(x, (int, float)) for x in numbers)

    # mean of the dataset
    mean = sum(numbers) / len(numbers)

    # absolute differences from mean (for all the integers)
    abs_deviations = [abs(x - mean) for x in numbers]

    # take the average of absolute differences (for all integers)
    return sum(abs_deviations) / len(numbers)

