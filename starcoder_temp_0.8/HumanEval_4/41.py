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

    # Get mean of the set of numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the sum of absolute differences between
    # the numbers and the mean
    m_abs_dev = 0
    for number in numbers:
        m_abs_dev += abs(number - mean)

    # Return the average of absolute differences as mean absolute deviation
    return m_abs_dev / len(numbers)
