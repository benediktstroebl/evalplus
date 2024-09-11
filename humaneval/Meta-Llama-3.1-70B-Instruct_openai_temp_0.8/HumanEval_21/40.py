```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): List of numbers to rescale.

    Returns:
        List[float]: Rescaled list of numbers.

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        return [1.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function, which takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest number is 1. It first checks if the input list has at least two elements, raising a `ValueError` if not. Then, it calculates the minimum and maximum values in the list. If the minimum and maximum values are equal, it returns a list of 1.0s with the same length as the input list. Otherwise, it applies a linear transformation to each number in the list using a list comprehension and returns the result.