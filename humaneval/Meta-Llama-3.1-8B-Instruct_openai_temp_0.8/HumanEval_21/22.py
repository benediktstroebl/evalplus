```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: The rescaled list of float numbers

    Raises:
        ValueError: If the list contains less than two elements

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # If all elements are equal, return a list of zeros
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform to the list
    rescaled = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of float numbers, applies a linear transform to it, and returns the rescaled list. The transform is done by scaling each number to a value between 0 and 1, where the smallest number in the list becomes 0 and the largest number becomes 1. The script also includes a docstring with example usage, argument and return value descriptions, and a `ValueError` exception for lists with less than two elements. It also includes a test case at the end to demonstrate the function's behavior.