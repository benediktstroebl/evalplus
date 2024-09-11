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
        float: The Mean Absolute Deviation.
    """
    # Calculate the mean of the given numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = statistics.mean(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation of {numbers} is {mad}")
```

In this script, we use the `statistics` module to calculate the mean of the input numbers. Then, we use a list comprehension to calculate the absolute difference between each element and the mean. Finally, we use the `statistics.mean` function again to calculate the Mean Absolute Deviation.

The example usage shows how to use the `mean_absolute_deviation` function with a list of numbers and print the result.