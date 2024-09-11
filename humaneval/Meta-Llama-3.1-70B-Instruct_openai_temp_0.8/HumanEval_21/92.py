```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of floating point numbers.

    Returns:
        A new list where the smallest number is 0 and the largest is 1.

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        # If all numbers are the same, return a list of zeros.
        return [0.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest is 1. The function first checks if the input list has at least two elements, and if not, it raises a `ValueError`. It then finds the minimum and maximum values in the list, and uses these to calculate the rescaled values for each number in the list. The rescaled values are calculated using a list comprehension, which is a concise way to create a new list by applying a transformation to each element of an existing list.