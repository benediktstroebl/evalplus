```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the input list has less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers in the list are the same
    if min_value == max_value:
        # If all numbers are the same, return a list of zeros
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(n - min_value) / (max_value - min_value) for n in numbers]

    return rescaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of float numbers as input, applies a linear transform to the list, and returns the rescaled list. The transform maps the smallest number in the list to 0 and the largest number to 1. If the input list has less than two elements, the function raises a `ValueError`. The script also includes a test case for the function.