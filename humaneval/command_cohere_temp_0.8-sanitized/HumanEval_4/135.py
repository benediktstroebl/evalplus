from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
   Args:
        numbers (List[float]): List of numerical data.
    Returns:
        float: Mean Absolute Deviation score.
    """
    mean = sum(numbers) / len(numbers)
    deviation = sum(abs(x - mean) for x in numbers)
    return deviation / len(numbers)