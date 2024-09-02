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

    numbers.sort()
    n = len(numbers)

    for i in range(1, n):
        for j in range(i, n):
            difference = numbers[i] - numbers[j]
            numbers[i] = numbers[j]
            numbers[j] = difference

    return numbers[n - 1]

