```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of rescaled floating point numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if min_val == max_val:
        raise ValueError("All numbers in the list are equal")

    return [(num - min_val) / (max_val - min_val) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input, and returns a new list with the same numbers but rescaled to the range [0, 1]. The rescaling is done by subtracting the smallest number in the list from each number to shift the range to [0, range], and then dividing by the range to get the desired [0, 1] range.

The script includes a docstring that describes the function's behavior, including an example usage, and raises a `ValueError` if the input list has less than two elements or if all numbers in the list are equal, to prevent division by zero.