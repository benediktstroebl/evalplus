### Rescaling a List of Numbers to Unit Range
#### Problem Description
Given a list of numbers, apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.

#### Solution

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the input list contains less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        # Handle the case when all numbers are the same
        return [0.0] * len(numbers)

    # Calculate the rescaled values
    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled

# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers, but scaled to the unit range [0, 1]. The function raises a `ValueError` if the input list contains less than two elements.