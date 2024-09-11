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

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    if max_value == min_value:
        raise ValueError("All numbers are the same")

    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and applies a linear transformation to rescale them between 0 and 1. The function first checks if the list contains at least two elements and if all numbers are different. It then calculates the minimum and maximum values in the list and applies the linear transformation to each number. The result is a new list where the smallest number is 0 and the largest number is 1.