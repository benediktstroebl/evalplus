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
        Mean Absolute Deviation of the input numbers.
    """
    
    # Check if input list is empty
    if not numbers:
        raise ValueError("Input list is empty")
    
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    result = mean_absolute_deviation(numbers)
    print(f"Mean Absolute Deviation of {numbers}: {result}")
```

This Python script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It first checks if the input list is empty, then calculates the mean of the input numbers, the absolute differences between each element and the mean, and finally the mean of these absolute differences. The result is returned by the function.

In the example usage section, we demonstrate how to use this function with a sample list of numbers and print the result.