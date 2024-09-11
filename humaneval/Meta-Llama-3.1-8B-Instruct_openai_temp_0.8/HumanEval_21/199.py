```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): The list of numbers to be rescaled.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        raise ValueError("All elements in the list are the same")

    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of floating point numbers, finds the minimum and maximum values in the list, and then applies a linear transformation to each number in the list such that the smallest number becomes 0 and the largest number becomes 1. It includes error checking to ensure the input list has at least two elements and returns a `ValueError` if the input list does not meet this requirement.