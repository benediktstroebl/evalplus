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
    length = float(len(numbers))

    if length < 2:
        raise ValueError('Length of list should be at least 2')

    s = sum(numbers)
    deviations = [number - s / length for number in numbers]
    abs_deviations = [abs(deviation) for deviation in deviations]
    mad = sum(abs_deviations) / length
    return round(mad, 2)

