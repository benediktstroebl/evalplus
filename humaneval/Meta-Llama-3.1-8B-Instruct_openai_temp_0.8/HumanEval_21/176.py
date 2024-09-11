```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = np.min(numbers)
    max_value = np.max(numbers)

    # Check if all numbers are equal
    if min_value == max_value:
        # If all numbers are equal, return a list with all elements equal to 0
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(n - min_value) / (max_value - min_value) for n in numbers]

    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script uses a list comprehension to apply the linear transform to each number in the input list. It first checks if the list has at least two elements, and if it does not, it raises a ValueError. Then it finds the minimum and maximum values in the list, and checks if all numbers are equal. If all numbers are equal, it returns a list with all elements equal to 0. Otherwise, it applies the linear transform to each number and returns the rescaled list.