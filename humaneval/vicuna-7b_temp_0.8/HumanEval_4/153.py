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

    def get_dev(val, mean):
        abs_val = abs(val - mean)
        return abs_val

    def avg_dev(list_dev):
        return sum(list_dev) / len(list_dev)

    dev_list = [get_dev(val, sum(numbers)) for val in numbers]
    avg_dev = avg_dev(dev_list)
    return avg_dev

