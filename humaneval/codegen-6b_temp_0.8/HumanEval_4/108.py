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
    # Extract the list of numbers
    samples = numbers
    # The mean of the set of numbers
    mean = float(sum(samples)) / float(len(samples))
    # Calculate the deviation of each element from the mean
    # Absolute value allows negative numbers
    absolute_deviations = [abs(sample - mean) for sample in samples]
    # Add them to get the mean absolute deviation
    deviations_from_mean = sum(absolute_deviations) / float(len(absolute_deviations))
    return deviations_from_mean

