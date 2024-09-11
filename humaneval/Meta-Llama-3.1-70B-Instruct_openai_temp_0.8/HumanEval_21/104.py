```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floats with at least two elements.

    Returns:
        A list of floats where the smallest number in the input list is 0 and the largest is 1.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    if range_value == 0:
        return [1.0] * len(numbers)  # if all numbers are the same, return a list of 1.0

    return [(x - min_value) / range_value for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the function `rescale_to_unit` that takes a list of floats as input and returns a new list where the smallest number is 0 and the largest is 1. The function first checks if the input list has at least two elements, and if not, raises a ValueError. It then calculates the minimum and maximum values in the list and the range of values. If the range is 0 (i.e., all numbers are the same), it returns a list of 1.0. Otherwise, it uses a list comprehension to apply the linear transformation to each number in the list. Finally, it includes an example usage of the function.