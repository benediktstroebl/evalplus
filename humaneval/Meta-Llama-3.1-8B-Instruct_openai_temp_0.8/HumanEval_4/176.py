### Mean Absolute Deviation Calculator

The following Python script calculates the Mean Absolute Deviation from a given list of numbers.

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
    numbers (List[float]): A list of numbers.
    
    Returns:
    float: The Mean Absolute Deviation.
    """
    
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]
    
    # Calculate the average of these differences
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
print(mean_absolute_deviation([5.0, 10.0, 15.0, 20.0]))  # Output: 5.0
```

### Step-by-Step Solution:

1.  Define a function `mean_absolute_deviation` that takes a list of numbers as input.
2.  Calculate the mean of the input numbers by summing them up and dividing by the total count.
3.  Calculate the absolute differences between each number and the mean using a list comprehension.
4.  Calculate the Mean Absolute Deviation (MAD) by averaging the absolute differences.
5.  Return the MAD value.

This solution provides a clear and concise implementation of the Mean Absolute Deviation calculation in Python.