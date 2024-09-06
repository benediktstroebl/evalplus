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
    # When given a list of numbers, you can get the mean of the list and
    # calculate the difference between each element and the mean.
    # For each element, the absolute difference is calculated.
    # Then, the average deviation is taken over each element.
    mean_of_values = sum(numbers) / len(numbers)

    deviations = [(abs(n - mean_of_values)) for n in numbers]
    return sum(deviations) / len(numbers)

