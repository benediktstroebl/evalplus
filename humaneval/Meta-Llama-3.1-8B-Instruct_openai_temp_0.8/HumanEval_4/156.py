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
        numbers (List[float]): A list of float numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = statistics.mean(deviations)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This Python script calculates the Mean Absolute Deviation of a list of numbers. The `mean_absolute_deviation` function takes a list of floats as input, calculates the mean of the numbers, and then calculates the absolute deviations of each number from the mean. Finally, it calculates the mean of these deviations, which is the Mean Absolute Deviation. The example usage at the end demonstrates how to use the function with a sample list of numbers.