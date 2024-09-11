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
        numbers (List[float]): A list of numbers.
    
    Returns:
        float: The Mean Absolute Deviation.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
```

In this script, we define the `mean_absolute_deviation` function that takes a list of numbers as input, calculates the mean, then calculates the absolute difference between each number and the mean. Finally, it calculates the Mean Absolute Deviation by taking the average of these absolute differences. The script also includes example usage and error handling for an empty input list.