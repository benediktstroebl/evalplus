from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Ensure the input list is not empty and all elements are floats
    if not numbers or not all(isinstance(n, float) for n in numbers):
        raise ValueError("Input list must be a non-empty list of floats")
        
    # Calculate mean and deviation
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    return sum(absolute_deviations) / len(numbers)