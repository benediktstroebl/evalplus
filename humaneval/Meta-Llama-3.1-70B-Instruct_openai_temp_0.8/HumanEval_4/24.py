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
        float: The Mean Absolute Deviation of the input numbers.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the numbers
    mean = statistics.mean(numbers)

    # Calculate the absolute difference between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = statistics.mean(absolute_differences)

    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation around the mean of the dataset. The function uses the `statistics` module to calculate the mean of the numbers and then calculates the absolute difference between each number and the mean. Finally, it returns the mean of the absolute differences. The script also includes a test case to demonstrate the function's usage.