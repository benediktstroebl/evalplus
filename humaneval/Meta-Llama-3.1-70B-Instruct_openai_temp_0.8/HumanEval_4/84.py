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
    # Calculate the mean of the dataset
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of these absolute differences
    mad = statistics.mean(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. It first calculates the mean of the dataset using the `statistics.mean` function, then calculates the absolute difference between each element and the mean using a list comprehension. Finally, it calculates the mean of these absolute differences to get the MAD.

You can run this script and use the `mean_absolute_deviation` function to calculate the MAD of any list of numbers.