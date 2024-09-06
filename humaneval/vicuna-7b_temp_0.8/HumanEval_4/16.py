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
    # The mean of the input numbers
    mean = float(sum(numbers)) / len(numbers)

    # The squared difference of each number from its mean
    dev = [abs(x - mean) for x in numbers]
    dev_sum = sum(dev)

    # Calculate the mean of squared differences
    mean_squared_dev = dev_sum / len(dev)

    # The MAD is the average of the squared differences
    return (mean_squared_dev * 2) ** 0.5
