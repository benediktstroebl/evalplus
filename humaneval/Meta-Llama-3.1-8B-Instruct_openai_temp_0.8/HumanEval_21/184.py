```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): The list of numbers to be rescaled.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # Check if the minimum and maximum values are equal
    if min_val == max_val:
        raise ValueError("The input list must have at least two distinct elements.")

    # Apply the linear transform to the list
    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been rescaled to the range [0, 1]. It uses the `numpy` library to find the minimum and maximum values in the list and applies a linear transform to the list using a list comprehension. The function also includes input validation to ensure that the list has at least two elements and that the minimum and maximum values are distinct.