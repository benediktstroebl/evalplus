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
    # Find the mean of the input numbers
    num_sum = sum(numbers)
    if num_sum == 0:
        return 0
    mean = num_sum / len(numbers)
    # Calculate the MAD
    i = 0
    deviations = []
    while i < len(numbers) - 1:
        deviations.append(abs(numbers[i] - mean))
        i += 1
    deviations.append(abs(numbers[-1] - mean))
    deviation_sum = sum(deviations)
    if deviation_sum == 0:
        return 0
    else:
        return deviation_sum / (len(deviations) - 1)

