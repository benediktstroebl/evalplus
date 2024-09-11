```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of float numbers.

    Returns:
        A list of float numbers where the smallest number is 0 and the largest is 1.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same (to avoid division by zero)
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    rescaled_numbers = [(n - min_value) / (max_value - min_value) for n in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines the `rescale_to_unit` function that takes a list of float numbers as input, applies a linear transformation to scale the numbers between 0 and 1, and returns the rescaled list. The script includes error handling to ensure the input list has at least two elements and handles the case where all numbers are the same. The example usage demonstrates how to use the `rescale_to_unit` function.