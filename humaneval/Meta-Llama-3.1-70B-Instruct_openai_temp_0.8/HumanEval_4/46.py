```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.
    
    The Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.
    
    Args:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input numbers.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    mad = mean_absolute_deviation(numbers)
    print(f"The Mean Absolute Deviation of {numbers} is {mad}")
```

This script defines a function `mean_absolute_deviation` that takes a list of floating point numbers as input and returns the Mean Absolute Deviation of the input numbers. It uses a list comprehension to calculate the absolute differences between each element and the mean, and then calculates the Mean Absolute Deviation as the average of these differences.

In the example usage section, we demonstrate how to use the `mean_absolute_deviation` function with a sample list of numbers.