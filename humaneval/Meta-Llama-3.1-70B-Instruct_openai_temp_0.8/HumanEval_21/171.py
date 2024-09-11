```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of at least two float numbers.

    Returns:
        List[float]: The rescaled list of numbers.
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # If all numbers are the same, return a list of zeros with the last element as 1
    if value_range == 0:
        return [0.0] * (len(numbers) - 1) + [1.0]

    # Apply the linear transformation
    return [(num - min_value) / value_range for num in numbers]

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function, which takes a list of float numbers as input and returns a new list where the smallest number is rescaled to 0 and the largest number is rescaled to 1. The function first checks if the input list has at least two elements, then finds the minimum and maximum values in the list. It calculates the range of the values and applies a linear transformation to each number in the list. If all numbers in the list are the same, the function returns a list of zeros with the last element as 1.