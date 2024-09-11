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
    """
    # Calculate the mean of the input numbers
    mean_value = statistics.mean(numbers)
    
    # Calculate the absolute differences between each number and the mean
    absolute_differences = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)
    
    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script calculates the Mean Absolute Deviation (MAD) around the mean of a dataset. The `mean_absolute_deviation` function first calculates the mean of the input numbers, then calculates the absolute differences between each number and the mean, and finally calculates the mean of these absolute differences. The result is the Mean Absolute Deviation.