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
        numbers: A list of float numbers.
    
    Returns:
        The Mean Absolute Deviation of the input list.
    
    Raises:
        ValueError: If the input list is empty.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(result)  # Output: 1.0
```

In this script, we define the `mean_absolute_deviation` function that takes a list of numbers as input and returns the Mean Absolute Deviation. We first calculate the mean of the input list, then calculate the absolute difference between each element and the mean, and finally calculate the mean of these absolute differences.

The script also includes a check for an empty input list, raising a `ValueError` if the list is empty. The example usage at the end demonstrates how to use the function with a sample list of numbers.