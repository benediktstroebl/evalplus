```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of float numbers

    Returns:
        A list of float numbers rescaled to the unit interval [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_val == max_val:
        # If they are the same, return a list with all elements equal to 0
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers as input and returns a new list with the same numbers rescaled to the unit interval [0, 1]. The function first checks if the input list has at least two elements. If not, it raises a `ValueError`. Then it finds the minimum and maximum values in the list and applies a linear transform to each number in the list. The transform maps the minimum value to 0 and the maximum value to 1. If all numbers in the list are equal, the function returns a list with all elements equal to 0. The script includes a test case to demonstrate the function's behavior.