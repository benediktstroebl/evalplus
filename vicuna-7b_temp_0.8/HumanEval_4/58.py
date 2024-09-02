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
    # get the mean of the input numbers
    num_sum = sum(numbers)
    mean = numbers.pop(0)
    num_list = [x - mean for x in numbers]
    num_list.append(0)  # add 0 to get a list of absolute differences
    total_deviation = sum(num_list)
    return total_deviation

