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
    # TODO: Check input for type of `list`
    assert isinstance(numbers, list), 'Input is not of type list'

    mean = sum(numbers) / len(numbers)
    abs_diff = map(lambda number: abs(number - mean), numbers)
    return sum(abs_diff) / len(numbers)

