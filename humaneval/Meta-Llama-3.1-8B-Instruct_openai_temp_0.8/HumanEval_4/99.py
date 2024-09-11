```markdown
### Mean Absolute Deviation Calculator

#### Problem Description
For a given list of input numbers, calculate Mean Absolute Deviation
around the mean of this dataset.

#### Formula
Mean Absolute Deviation is the average absolute difference between each
element and a centerpoint (mean in this case):
MAD = average | x - x_mean |

#### Solution
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        float: The Mean Absolute Deviation of the input numbers.

    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    # Calculate the mean of the input numbers
    mean_value = sum(numbers) / len(numbers)
    
    # Initialize a variable to store the sum of absolute deviations
    total_absolute_deviation = 0
    
    # Iterate over each number in the input list
    for num in numbers:
        # Calculate the absolute deviation for the current number
        absolute_deviation = abs(num - mean_value)
        
        # Add the absolute deviation to the total
        total_absolute_deviation += absolute_deviation
    
    # Calculate the Mean Absolute Deviation
    mad = total_absolute_deviation / len(numbers)
    
    return mad
```

#### Example Usage
```python
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script defines a function `mean_absolute_deviation` that takes a list of float numbers as input and returns their Mean Absolute Deviation. The function first calculates the mean of the input numbers, then iterates over each number to calculate its absolute deviation from the mean. The sum of these absolute deviations is divided by the total count of numbers to obtain the Mean Absolute Deviation. The example usage demonstrates how to call the function with a sample list of numbers.