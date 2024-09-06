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
    if len(numbers) < 2:
        return 0.0
    
    sum_of_square_errors = 0.0
    for num in numbers:
        sum_of_square_errors += (num - numbers[0]) ** 2
    
    avg_of_square_errors = sum_of_square_errors / len(numbers)
    sum_of_absolute_errors = 0.0
    for num in numbers:
        sum_of_absolute_errors += abs(num - numbers[0])
    
    return sum_of_absolute_errors / len(numbers)

