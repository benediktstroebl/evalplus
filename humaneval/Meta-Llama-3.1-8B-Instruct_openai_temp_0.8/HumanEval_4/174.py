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
    numbers (List[float]): The list of numbers to calculate Mean Absolute Deviation for.

    Returns:
    float: The Mean Absolute Deviation of the input list.
    """
    
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns their Mean Absolute Deviation. It first calculates the mean of the input list, then computes the absolute deviation from the mean for each number. Finally, it calculates the mean of these absolute deviations to obtain the Mean Absolute Deviation. The function includes a docstring with a description, example usage, and a list of arguments and return values for clarity. The script also includes an example usage at the end to demonstrate how to call the function with a sample list of numbers.