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
    number_set = set(numbers)
    number_list = list(number_set)
    sort_list = sorted(number_list)
    center_point = round(sum(number_list) / len(number_list), 2)
    index_value = [abs(x - center_point) for x in sort_list]
    return round(sum(index_value) / len(index_value), 2)

