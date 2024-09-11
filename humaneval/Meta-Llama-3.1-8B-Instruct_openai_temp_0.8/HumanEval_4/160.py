### Mean Absolute Deviation Calculation
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
        numbers (List[float]): A list of numbers for which to calculate MAD.

    Returns:
        float: The mean absolute deviation of the input numbers.
    """
    
    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation for each number from the mean
    deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(deviations) / len(deviations)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print("Mean Absolute Deviation:", mean_absolute_deviation(numbers))
```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. The MAD is calculated as the average absolute difference between each number in the list and the mean of the list. The function takes a list of numbers as input and returns the calculated MAD. An example usage of the function is provided at the end of the script.