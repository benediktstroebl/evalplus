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
    # Check input
    if len(numbers) < 1:
        raise ValueError("Input must contain at least one number.")

    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate absolute deviations from mean
    deviations = []
    for number in numbers:
        deviations.append(abs(number - mean))

    # Return mean absolute deviation
    return sum(deviations) / len(numbers)

