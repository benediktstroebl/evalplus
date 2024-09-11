```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the input list has less than two elements.

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value
    if range_value == 0:  # To avoid division by zero
        return [0.0] * len(numbers)

    return [(x - min_value) / range_value for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

This Python script defines a function `rescale_to_unit` that rescales a given list of numbers to the unit interval [0, 1]. It first checks if the input list has at least two elements and raises a `ValueError` if it doesn't. Then, it finds the minimum and maximum values in the list, calculates the range, and applies a linear transformation to each element in the list. The result is a new list where the smallest number is 0 and the largest number is 1. If the range is 0 (i.e., all elements are the same), the function returns a list of zeros. The example usage demonstrates how to use this function with a list of numbers.