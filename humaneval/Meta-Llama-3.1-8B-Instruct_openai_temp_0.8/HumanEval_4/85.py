```python
from typing import List

def calculate_mean(numbers: List[float]) -> float:
    """ Calculate the mean of a list of numbers.
    
    Args:
    numbers (List[float]): A list of numbers.
    
    Returns:
    float: The mean of the numbers.
    """
    return sum(numbers) / len(numbers)


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    
    Args:
    numbers (List[float]): A list of numbers.
    
    Returns:
    float: The mean absolute deviation of the numbers.
    """
    mean_value = calculate_mean(numbers)
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

This script defines two functions: `calculate_mean` to calculate the mean of a list of numbers, and `mean_absolute_deviation` to calculate the mean absolute deviation of a list of numbers. The example usage at the end shows how to use these functions to calculate the mean absolute deviation of the list `[1.0, 2.0, 3.0, 4.0]`.