```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
    numbers (List[float]): A list of numbers.

    Returns:
    List[float]: The rescaled list of numbers.
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number is mapped to 0 and the largest number is mapped to 1. The function first checks if the input list contains at least two elements and raises a `ValueError` otherwise. It then finds the minimum and maximum values in the list. If the minimum and maximum values are equal, it returns a list of zeros to avoid division by zero. Finally, it applies the linear transformation using a list comprehension and returns the result.