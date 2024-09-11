```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: The transformed list of numbers.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same, to avoid division by zero
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers, finds the minimum and maximum values, and applies a linear transformation to map the smallest number to 0 and the largest to 1. It includes error checking to ensure the input list has at least two elements and handles the case where all numbers are the same. The example usage demonstrates the function's behavior with a sample list of numbers.