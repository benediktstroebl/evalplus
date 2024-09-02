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
    # Calculate mean and standard deviation
    mean = sum(numbers) / len(numbers)
    variance = sum([(num - mean) ** 2 for num in numbers]) / len(numbers)
    
    # Calculate absolute values of deviations from the mean
    abstdev = [abs(num - mean) for num in numbers]
    
    # Calculate MAD using sum of deviations divided by number of variables
    MAD = sum(abstdev) / len(numbers)
    return MAD

