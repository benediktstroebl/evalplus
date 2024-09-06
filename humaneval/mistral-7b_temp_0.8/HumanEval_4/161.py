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
    #  TODO: Implement this function
    #  Think about what steps you need to follow to implement this function.
    #  What do you need to do?
    #  How would you do it?

    #  Put your code below
    sum = 0
    for number in numbers:
        sum += abs(number - sum / len(numbers))
    return sum / len(numbers)
