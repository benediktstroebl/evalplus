```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation of a dataset.
    
    Mean Absolute Deviation is the average absolute difference between each element
    and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
    numbers (List[float]): A list of float numbers.

    Returns:
    float: The Mean Absolute Deviation of the given numbers.

    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    
    # Calculate the mean of the numbers
    mean_value = sum(numbers) / len(numbers)
    
    # Calculate the absolute differences between each number and the mean
    absolute_deviations = [abs(num - mean_value) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input and returns the Mean Absolute Deviation of the dataset. It uses list comprehension to calculate the absolute differences between each number and the mean, then calculates the mean of these absolute deviations. The function is then tested with the example list `[1.0, 2.0, 3.0, 4.0]`.