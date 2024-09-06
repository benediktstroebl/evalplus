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
    # TODO: Your code here
    # print(numbers)
    number_sum = sum(numbers)
    number_count = len(numbers)
    mean = number_sum/number_count
    # print(mean)
    absolute_differences = [abs(number - mean) for number in numbers]
    # print(absolute_differences)
    return sum(absolute_differences)/len(absolute_differences)

