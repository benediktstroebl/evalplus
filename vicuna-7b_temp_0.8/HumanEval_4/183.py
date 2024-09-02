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
    data = list(numbers)
    # sort the list
    data.sort()
    # calculate the mean
    mean = sum(data)/len(data)
    # calculate the deviation for each value
    deviations = [abs(x-mean) for x in data]
    # calculate the average of the deviations
    return sum(deviations)/len(data)

