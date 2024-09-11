```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) around the mean of a dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.

    Raises:
    ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences from the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines the `mean_absolute_deviation` function that calculates the Mean Absolute Deviation of a given list of numbers. The function first checks if the input list is not empty. It then calculates the mean of the numbers, computes the absolute differences from the mean, and finally calculates the mean of these absolute differences. The result is returned as a float. The example usage at the end demonstrates how to use the function with a sample list of numbers.