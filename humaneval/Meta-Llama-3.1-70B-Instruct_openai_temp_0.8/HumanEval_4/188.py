```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The mean absolute deviation of the input numbers.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")
    
    # Calculate the mean of the numbers
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_differences = [abs(x - mean_value) for x in numbers]
    
    # Return the mean of the absolute differences
    return statistics.mean(absolute_differences)


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)  # Output: 1.0
```