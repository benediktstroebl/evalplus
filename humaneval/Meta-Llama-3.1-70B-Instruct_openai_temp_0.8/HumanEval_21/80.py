```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floats with at least two elements

    Returns:
        A list of floats where the smallest number is 0 and the largest is 1
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floats as input and returns a new list with the same length, where the smallest number in the input list is mapped to 0 and the largest number is mapped to 1. The function first checks if the input list has at least two elements, and if not, raises a `ValueError`. It then finds the minimum and maximum values in the list, and if they are the same (i.e., all numbers are the same), returns a list of zeros with the same length as the input list. Otherwise, it applies a linear transformation to the input list using a list comprehension, and returns the resulting list.