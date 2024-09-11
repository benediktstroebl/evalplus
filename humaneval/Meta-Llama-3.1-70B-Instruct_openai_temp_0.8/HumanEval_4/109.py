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
        numbers (List[float]): A list of input numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.

    Raises:
        ValueError: If the input list is empty.
    """

    # Check if the list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(mad)  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. It first checks if the input list is empty, and if so, raises a `ValueError`. Then, it calculates the mean of the input list, followed by the absolute differences between each element and the mean. Finally, it calculates the Mean Absolute Deviation by averaging these absolute differences. The example usage demonstrates how to use this function with a sample list of numbers.