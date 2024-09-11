```python
from typing import List

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
        float: The mean absolute deviation.
    """
    
    # First, calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Initialize a variable to store the sum of absolute differences
    absolute_diff_sum = 0
    
    # Iterate over each number in the list
    for num in numbers:
        # Calculate the absolute difference between the current number and the mean
        absolute_diff = abs(num - mean)
        
        # Add the absolute difference to the sum
        absolute_diff_sum += absolute_diff
    
    # Calculate the mean absolute deviation by dividing the sum of absolute differences by the length of the list
    mad = absolute_diff_sum / len(numbers)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

Alternatively, you can use a more concise version using list comprehension and the built-in `statistics` module:

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
        float: The mean absolute deviation.
    """
    
    mean = statistics.mean(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```