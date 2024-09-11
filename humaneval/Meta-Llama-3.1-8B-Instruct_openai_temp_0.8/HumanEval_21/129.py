```python
from typing import List
import copy

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floats

    Returns:
        List[float]: The rescaled list of floats

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Create a copy of the list to avoid modifying the original list
    numbers_copy = copy.deepcopy(numbers)

    # Find the smallest and largest numbers in the list
    smallest_num = min(numbers_copy)
    largest_num = max(numbers_copy)

    # Check if the smallest and largest numbers are the same
    if smallest_num == largest_num:
        # If they are the same, return a list of zeros (or ones, it doesn't matter)
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(n - smallest_num) / (largest_num - smallest_num) for n in numbers_copy]

    return rescaled_numbers


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of floats as input and returns a new list where the smallest number is 0 and the largest number is 1. The function uses a linear transform to achieve this. It also includes a check to ensure the input list has at least two elements, and handles the case where the smallest and largest numbers are the same. The script includes a test case to demonstrate the function's behavior.