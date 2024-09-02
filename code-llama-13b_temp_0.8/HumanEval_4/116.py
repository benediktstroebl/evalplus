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
    # Calculate the average of our dataset
    mean = sum(numbers) / len(numbers)

    # Calculate absolute differences between the mean and every element in the list
    absolute_differences_from_mean = [abs(mean - number) for number in numbers]

    # Sum up all of the absolute differences and divide by the length of the list
    sum_absolute_differences = sum(absolute_differences_from_mean)
    return sum_absolute_differences / len(numbers)

