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
    # TODO: Fill in this function to return the Mean Absolute Deviation
    #       of the given list of numbers.
    #       The MAD can be calculated by:
    #       MAD = (sum | x_i - x_mean |) / N
    #       Where N is the number of elements in the input list.

    # Your code here
    # To get the mean:
    mean = sum(numbers) / len(numbers)
    # To get the deviation:
    deviation = [abs(i - mean) for i in numbers]
    # To get the mean of the deviation:
    return sum(deviation) / len(deviation)

