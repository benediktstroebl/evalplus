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
    float: The Mean Absolute Deviation of the input list.

    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Initialize sum of absolute differences to 0
    sum_of_abs_diff = 0
    
    # Iterate over each number in the list
    for num in numbers:
        # Calculate the absolute difference between the number and the mean
        abs_diff = abs(num - mean)
        
        # Add the absolute difference to the sum
        sum_of_abs_diff += abs_diff
    
    # Calculate the Mean Absolute Deviation by dividing the sum of absolute
    # differences by the number of elements
    mad = sum_of_abs_diff / len(numbers)
    
    return mad

# Test the function with a list of numbers
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation of a given list of numbers. The function works by first calculating the mean of the input list, then iterating over each number in the list to calculate the absolute difference between the number and the mean, and finally returning the average of these absolute differences. The script includes a test case to demonstrate the function's usage.