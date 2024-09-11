```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` which takes a list of floats, finds the minimum and maximum values, and then applies a linear transformation to each value in the list, such that the smallest value becomes 0 and the largest value becomes 1. The script also includes an example usage of the function.