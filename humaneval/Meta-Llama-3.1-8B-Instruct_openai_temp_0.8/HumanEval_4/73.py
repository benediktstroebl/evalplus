### Mean Absolute Deviation Calculator
#### Python Implementation
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

    Mean Absolute Deviation is the average absolute difference between each element
    and the mean of the dataset.

    Args:
        numbers (List[float]): A list of floating-point numbers.

    Returns:
        float: The Mean Absolute Deviation.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Initialize a variable to store the sum of absolute differences
    absolute_diff_sum = 0

    # Iterate over each number in the input list
    for num in numbers:
        # Calculate the absolute difference between the current number and the mean
        absolute_diff = abs(num - mean)
        
        # Add the absolute difference to the sum
        absolute_diff_sum += absolute_diff

    # Calculate the Mean Absolute Deviation
    mad = absolute_diff_sum / len(numbers)

    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The function first calculates the mean of the input numbers, then iterates over each number to calculate its absolute difference from the mean and sums up these differences. Finally, it returns the sum of absolute differences divided by the total count of numbers, which is the definition of the Mean Absolute Deviation.