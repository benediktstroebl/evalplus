### Rescale List of Numbers to Unit Interval
```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): The list of numbers to rescale.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Ensure the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = np.min(numbers)
    max_value = np.max(numbers)

    # Apply the linear transform
    rescaled = [(num - min_value) / (max_value - min_value) for num in numbers]

    return rescaled

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns the same list, but with each number scaled to the unit interval [0, 1]. It uses NumPy to find the minimum and maximum values in the input list, and then applies a linear transform to each number to scale it to the unit interval. The function raises a `ValueError` if the input list has less than two elements, since scaling requires at least two distinct values.