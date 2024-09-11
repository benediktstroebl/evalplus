### Mean Absolute Deviation Calculator
```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each 
    element and a centerpoint (mean in this case):

    MAD = (1/n) * sum_i |x_i - x_mean|

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: Mean Absolute Deviation of the input list.
    """

    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate mean of the input list
    mean = statistics.mean(numbers)
    
    # Calculate absolute differences from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate mean of the absolute deviations
    mad = statistics.mean(absolute_deviations)
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Expected output: 1.0
```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It uses the `statistics` module to simplify the calculation of the mean. The function first checks if the input list is empty, raises a `ValueError` in this case, and then calculates the mean of the input list. It then calculates the absolute differences from the mean and finally calculates the mean of these absolute deviations, which is the Mean Absolute Deviation.

The script also includes a test case at the end to demonstrate the usage of the function. You can replace the `numbers` list with your own data to calculate the Mean Absolute Deviation.