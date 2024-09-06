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
    # The central point x_mean of the set of numbers (MAD center point)
    x_mean = sum(numbers) / len(numbers)

    # The absolute difference of each input number from x_mean
    deviations = [abs(n - x_mean) for n in numbers]

    # Return the mean of these deviations
    return sum(deviations) / len(deviations)

