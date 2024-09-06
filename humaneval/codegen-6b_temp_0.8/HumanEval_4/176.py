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
    lst = sorted(numbers)
    length = len(lst)
    if length % 2 == 0:
        # List of even numbers
        # Get M, the mean
        m = (lst[length / 2] + lst[length / 2 - 1]) / 2
        # Get centerpoint
        c = m - sum(lst[0:length / 2]) / length
        # Get the absolute difference between each element and the centerpoint
        results = [abs(x - c) for x in lst]
        # Get mean absolute difference
        mad = sum(results) / length
    else:
        # List of odd numbers
        # Create a list with the centerpoint
        center_point = lst[length / 2]
        # Get the absolute difference between each element and the centerpoint
        results = [abs(x - center_point) for x in lst]
        # Get mean absolute difference
        mad = sum(results) / length
    return mad

