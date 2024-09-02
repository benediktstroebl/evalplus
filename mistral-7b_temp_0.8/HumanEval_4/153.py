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
    num_list = []
    total = 0
    mean = 0
    for i in numbers:
        num_list.append(i)
    for i in num_list:
        total += i
    mean = total / len(numbers)
    res = 0
    for i in num_list:
        res += abs(i - mean)
    res = res / len(num_list)
    return res

