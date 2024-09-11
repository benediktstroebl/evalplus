```python
from typing import List
import numpy as np


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = np.min(numbers)
    max_value = np.max(numbers)

    # Check if all values are the same (to avoid division by zero)
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers and returns a new list where each number has been transformed to be between 0 and 1, inclusive. The transformation is a linear one, where the smallest original value becomes 0 and the largest becomes 1. The function also includes input validation to ensure that the list has at least two elements. If the list has less than two elements, it raises a `ValueError`. If all values in the list are the same, it returns a list of zeros to avoid division by zero.