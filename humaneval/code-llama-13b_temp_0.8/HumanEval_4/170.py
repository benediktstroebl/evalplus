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
    num_sum = 0
    if numbers:
        for num in numbers:
            num_sum += num
        mean = num_sum / len(numbers)
        sum1 = 0
        for num in numbers:
            sum1 += abs(num - mean)
        return sum1 / len(numbers)
    else:
        return 0.0

