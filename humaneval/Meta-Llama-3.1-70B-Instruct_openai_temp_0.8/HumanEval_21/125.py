```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers: A list of at least two float numbers.

    Returns:
    A new list with the same length as the input list, but with values 
    linearly transformed to the range [0, 1].
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Calculate the range of the input values
    value_range = max_value - min_value

    # If all values are the same, return a list of zeros (except the last one, which is 1)
    if value_range == 0:
        return [0.0] * (len(numbers) - 1) + [1.0]

    # Apply the linear transformation to each value in the list
    rescaled_numbers = [(value - min_value) / value_range for value in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers as input, applies a linear transformation to the list, and returns a new list with the transformed values. The transformation ensures that the smallest number becomes 0 and the largest becomes 1. The script also includes a docstring that provides documentation for the function, and an example usage at the end.