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
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script first calculates the mean of the input numbers using the `statistics.mean` function. It then calculates the absolute deviations from the mean by subtracting the mean from each number and taking the absolute value. Finally, it calculates the mean of the absolute deviations, which is the mean absolute deviation.

Note that this script uses list comprehension to calculate the absolute deviations, which is a concise and efficient way to perform this operation. It also uses the `statistics` module, which provides functions for calculating mathematical statistics such as the mean.