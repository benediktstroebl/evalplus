```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the input list contains less than two elements.
    """

    # Check if the input list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same to avoid division by zero
    if max_value == min_value:
        return [1.0] * len(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(num - min_value) / value_range for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input, applies a linear transformation to the list, and returns the rescaled list. The function first checks if the input list contains at least two elements, then finds the minimum and maximum values in the list. It calculates the range of the values and applies the linear transformation to each number in the list. The function returns the rescaled list of numbers. The script also includes an example usage of the function.