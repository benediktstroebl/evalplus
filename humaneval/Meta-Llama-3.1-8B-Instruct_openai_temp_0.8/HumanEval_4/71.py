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
        numbers (List[float]): A list of float numbers

    Returns:
        float: The Mean Absolute Deviation of the input numbers

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    
    # Check if the list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the list
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

In this script, we first define the `mean_absolute_deviation` function that takes a list of float numbers as input. We then calculate the mean of the input list, followed by the absolute difference between each element and the mean. Finally, we calculate the mean of these absolute deviations, which is the Mean Absolute Deviation (MAD). If the input list is empty, we raise a ValueError. The function is tested with the example given in the problem statement.