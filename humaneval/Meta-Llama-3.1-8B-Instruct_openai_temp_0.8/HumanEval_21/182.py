```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

    Returns:
        List[float]: The rescaled list

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:  # Avoid division by zero
        return [0.0] * len(numbers)

    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]
    return rescaled

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers, finds the minimum and maximum values, and then applies a linear transformation to each number in the list, such that the smallest number becomes 0 and the largest becomes 1. The function returns the rescaled list. It also includes error checking to ensure the list has at least two elements, and handles the case where all numbers are the same.