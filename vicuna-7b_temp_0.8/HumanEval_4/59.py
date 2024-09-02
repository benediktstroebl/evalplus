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
    n = len(numbers)
    sum_of_differences = sum([abs(x - numbers.mean()) for x in numbers])
    sum_of_squares = sum([(x - numbers.mean())**2 for x in numbers])
    variance = sum_of_squares / n
    return sum_of_differences / n

if __name__ == '__main__':
    numbers = List(range(1, 6))
    mad = mean_absolute_deviation(numbers)
    print(mad)