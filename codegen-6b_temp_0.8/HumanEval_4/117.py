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
    if not numbers:
        return None

    # mean = sum of values / len(values)
    m = sum(numbers) / len(numbers)

    # square_difference = (value - mean) ** 2 for each value
    squares = [float(x - m) ** 2 for x in numbers]
    return sum(squares) / len(numbers) ** 0.5

