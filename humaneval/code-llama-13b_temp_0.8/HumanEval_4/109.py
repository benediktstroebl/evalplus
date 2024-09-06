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
    # Create a list for the absolute differences between x_mean and each element
    absolute_differences = []
    # Get the mean of the input numbers
    x_mean = sum(numbers) / len(numbers)
    # Loop through each number in the input list
    for number in numbers:
        # Add the absolute value of the difference between x_mean and each element to absolute_differences
        absolute_differences.append(abs(number - x_mean))
    # Return the mean of the absolute differences
    return sum(absolute_differences) / len(absolute_differences)
