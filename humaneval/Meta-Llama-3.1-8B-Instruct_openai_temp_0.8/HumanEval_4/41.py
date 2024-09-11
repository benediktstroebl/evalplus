### Calculate Mean Absolute Deviation
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
    numbers (List[float]): A list of numbers

    Returns:
    float: The Mean Absolute Deviation of the input list
    """
    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)
    
    # Initialize the sum of absolute differences
    absolute_diff_sum = 0
    
    # Iterate over each number in the list
    for num in numbers:
        # Calculate the absolute difference between the number and the mean
        absolute_diff = abs(num - mean)
        # Add the absolute difference to the sum
        absolute_diff_sum += absolute_diff
    
    # Calculate the Mean Absolute Deviation
    mad = absolute_diff_sum / len(numbers)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script first calculates the mean of the input list, then iterates over each number in the list to calculate the absolute difference between the number and the mean. The sum of these absolute differences is then divided by the number of elements in the list to calculate the Mean Absolute Deviation.