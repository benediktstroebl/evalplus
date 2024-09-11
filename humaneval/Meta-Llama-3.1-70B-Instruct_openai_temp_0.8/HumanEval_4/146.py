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
        float: The Mean Absolute Deviation of the input list.
    """
    # Calculate the mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first calculates the mean of the input list using the `statistics.mean` function. Then, it calculates the absolute difference between each element and the mean using a list comprehension. Finally, it calculates the mean of the absolute deviations using `statistics.mean` again. The result is returned by the function.

The script also includes a test case at the end, which demonstrates how to use the function and verifies that it produces the expected output.