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
    num_list = sorted(numbers)
    num_list.append(num_list[-1])
    num_list = [x - x[num_list.index(x)] for x in num_list]
    average = sum(num_list) / len(num_list)
    return average

