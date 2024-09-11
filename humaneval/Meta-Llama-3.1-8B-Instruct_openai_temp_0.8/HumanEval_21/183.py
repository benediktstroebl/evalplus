```python
from typing import List
import numpy as np

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
        raise ValueError("The list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number in the original list is 0 and the largest number is 1. The function uses the `numpy` library to perform the rescaling operation.

The function first checks if the list has at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum values in the list. If the maximum and minimum values are the same, it returns a list of zeros.

Otherwise, it uses a list comprehension to apply the linear transform to each number in the list. The transform is calculated as `(n - min_val) / (max_val - min_val)`, where `n` is the current number, `min_val` is the minimum value, and `max_val` is the maximum value. This transform maps the smallest number to 0 and the largest number to 1.

Finally, the script tests the function with a list of numbers and prints the result.