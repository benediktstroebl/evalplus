```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: The rescaled list of numbers.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for the case where all numbers are equal to avoid division by zero
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(num - min_value) / value_range for num in numbers]

    return rescaled_numbers


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest is 1. It first checks if the input list has at least two elements and raises a `ValueError` if not. It then finds the minimum and maximum values in the list and calculates the range of the values. If all numbers are equal, it returns a list of zeros to avoid division by zero. Finally, it applies the linear transformation to each number in the list and returns the rescaled list. The example usage demonstrates how to use the function with a sample list of numbers.