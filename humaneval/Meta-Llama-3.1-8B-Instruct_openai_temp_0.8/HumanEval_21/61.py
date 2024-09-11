```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to rescale

    Returns:
        List[float]: Rescaled list of numbers

    Raises:
        ValueError: If the list contains less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        # If all numbers are the same, return a list of all zeros
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([10.0, 10.0]))
print(rescale_to_unit([1.0, 1.0, 1.0]))
```

This script defines the `rescale_to_unit` function which takes a list of numbers as input and returns a new list where the smallest number in the input list becomes 0 and the largest number becomes 1. The function handles edge cases where the list contains less than two elements or where all numbers are the same. It also includes docstrings and example usage.