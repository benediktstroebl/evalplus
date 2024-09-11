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
    numbers (List[float]): A list of floating point numbers.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute differences between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This Python script defines a function `mean_absolute_deviation` that takes a list of floating point numbers as input and returns their Mean Absolute Deviation. The function uses the `statistics` module to calculate the mean of the input numbers and then calculates the absolute differences between each number and the mean. The mean of these absolute differences is then calculated and returned as the Mean Absolute Deviation. The example usage at the end demonstrates how to use this function with a sample list of numbers.