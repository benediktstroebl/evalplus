from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate the Mean Absolute Deviation
    around the mean of the dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.

    Parameters:
        numbers (List[float]): A list of numerical data.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """
    mean = sum(numbers) / len(numbers)
    deviation = sum(abs(x - mean) for x in numbers)
    return deviation / len(numbers)
numbers = [1.0, 2.0, 3.0, 4.0]