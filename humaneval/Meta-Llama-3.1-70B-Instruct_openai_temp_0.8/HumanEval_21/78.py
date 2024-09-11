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
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for case where all elements are the same
    if min_value == max_value:
        return [1.0] * len(numbers)

    # Calculate the range of the input list
    range_value = max_value - min_value

    # Apply the linear transformation to the input list
    rescaled_numbers = [(num - min_value) / range_value for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines a function `rescale_to_unit` that takes a list of numbers as input, applies a linear transformation to it, and returns the rescaled list. The linear transformation maps the smallest number to 0 and the largest number to 1. The script includes error checking to ensure that the input list has at least two elements and handles the case where all elements are the same. The example usage demonstrates how to use the function and prints the rescaled list.