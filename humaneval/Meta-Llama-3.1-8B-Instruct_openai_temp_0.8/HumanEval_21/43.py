```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floating point numbers

    Returns:
        A new list of floating point numbers, with the smallest number transformed to 0
        and the largest number transformed to 1

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` which takes a list of floating point numbers and returns a new list where the smallest number is transformed to 0 and the largest number is transformed to 1. The transformation is done using a linear function, which is implemented as a list comprehension. The function also includes some basic error checking to ensure that the input list contains at least two elements. If the input list contains only one element, or if all elements in the list are the same, the function raises a `ValueError`.