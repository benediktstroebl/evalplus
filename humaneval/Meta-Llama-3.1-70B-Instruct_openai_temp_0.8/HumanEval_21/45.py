```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers with at least two elements

    Returns:
        List[float]: The rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [1.0] * len(numbers)  # If all numbers are equal, return a list of 1.0

    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input, applies a linear transformation to the list, and returns the rescaled list. The transformation maps the smallest number in the list to 0 and the largest number to 1. The script also includes a check to ensure the input list has at least two elements and handles the case where all numbers in the list are equal.