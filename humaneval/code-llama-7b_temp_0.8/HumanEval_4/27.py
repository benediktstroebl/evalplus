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
    numbers = sorted(numbers)
    # calculate the mean of the list
    mean = sum(numbers) / len(numbers)
    # variable to calculate the sum
    sum_of_absolute_deviations = 0
    # loop through the list of numbers
    for num in numbers:
        # use absolute value to find the difference
        # from the mean of the numbers
        # add it to the sum of absolute deviations
        sum_of_absolute_deviations += abs(num - mean)

    # divide the sum of absolute deviations
    # by the number of numbers
    return sum_of_absolute_deviations / len(numbers)

