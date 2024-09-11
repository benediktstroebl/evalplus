**Mean Absolute Deviation Calculator**
======================================

### Description

This Python script calculates the Mean Absolute Deviation (MAD) of a given list of numbers around their mean.

### Code

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
        numbers (List[float]): A list of floating point numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Check if the list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute differences between each number and the mean
    absolute_differences = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

### Explanation

1. The `mean_absolute_deviation` function takes a list of floating point numbers as input.
2. It first checks if the input list is empty, and raises a `ValueError` if it is.
3. It calculates the mean of the input numbers by summing them up and dividing by the count.
4. It calculates the absolute differences between each number and the mean using a list comprehension.
5. It calculates the Mean Absolute Deviation by summing up the absolute differences and dividing by the count.
6. The function returns the calculated Mean Absolute Deviation.