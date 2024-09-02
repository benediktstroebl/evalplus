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
    sorted_numbers = sorted(numbers)
    # if there is only one number, then return 0
    if len(sorted_numbers) == 1:
        return 0
    # first calculate the mean of the dataset
    mean = sum(sorted_numbers) / len(sorted_numbers)
    # now calculate the deviation for each element
    deviations = [deviation(x, mean) for x in sorted_numbers]
    return sum(deviations) / len(deviations)

