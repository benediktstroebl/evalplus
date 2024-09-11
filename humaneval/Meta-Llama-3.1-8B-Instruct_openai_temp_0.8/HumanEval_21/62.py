```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The list of numbers rescaled to unit

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        # Avoid division by zero and return all zeros
        return [0.0] * len(numbers)

    # Apply linear transformation
    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a list of the same numbers, but rescaled to be between 0 and 1. The script includes a docstring that explains how the function works and provides an example usage. The function first checks if the list has at least two elements, and raises a `ValueError` if it doesn't. Then it calculates the minimum and maximum values in the list, and applies a linear transformation to each number in the list. If the maximum and minimum values are the same, the function returns a list of all zeros to avoid division by zero. Finally, the script tests the function with a list of numbers and prints the result.