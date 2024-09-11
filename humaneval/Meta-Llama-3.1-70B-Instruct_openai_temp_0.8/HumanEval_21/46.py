```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: The transformed list of numbers.

    Raises:
        ValueError: If the input list has less than two distinct elements.
    """

    # Check if the list has at least two distinct elements
    if len(set(numbers)) < 2:
        raise ValueError("Input list must have at least two distinct elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # Apply the linear transformation to each number in the list
    transformed_numbers = [(num - min_value) / value_range for num in numbers]

    return transformed_numbers


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input, applies a linear transformation to the list, and returns the transformed list. The transformation is done such that the smallest number in the list becomes 0 and the largest number becomes 1. The script also includes a check to ensure that the input list has at least two distinct elements. If the list has less than two distinct elements, the function raises a `ValueError`.