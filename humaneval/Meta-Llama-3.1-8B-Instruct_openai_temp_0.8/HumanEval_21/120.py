### Rescale Numbers to Unit Interval
#### A Python Function to Transform a List of Numbers to the Interval [0, 1]

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

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        return [0.0] * len(numbers)

    return [(n - min_value) / (max_value - min_value) for n in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number is transformed to 0 and the largest number is transformed to 1. The transformation is done through a linear mapping of the input values to the range [0, 1]. If the input list contains less than two elements, a `ValueError` is raised. If all numbers in the input list are identical, the output list will contain all zeros.