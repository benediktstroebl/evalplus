```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a dataset.
    
    MAD is the average absolute difference between each element and the mean of the dataset.
    
    Args:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    float: The Mean Absolute Deviation of the input dataset.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")
    
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences (MAD)
    mad = sum(absolute_diffs) / len(absolute_diffs)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines a function `mean_absolute_deviation` that takes a list of floating point numbers as input and returns the Mean Absolute Deviation (MAD) of the dataset. It calculates the mean of the dataset, then for each element, calculates the absolute difference between the element and the mean. Finally, it calculates the mean of these absolute differences, which is the MAD.

The script also includes an example usage of the function, demonstrating how to calculate the MAD of a sample dataset.