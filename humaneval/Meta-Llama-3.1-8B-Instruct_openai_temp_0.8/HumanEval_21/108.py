```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the input list has less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num - min_num == 0:
        # If all numbers are the same, return a list of the same value
        return [numbers[0]] * len(numbers)
    else:
        # Apply linear transformation to the list of numbers
        return [(num - min_num) / (max_num - min_num) for num in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))
print(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number is 0 and the largest number is 1. The function first checks if the input list has at least two elements, and raises a `ValueError` if not. It then calculates the minimum and maximum numbers in the list, and applies a linear transformation to the list to rescale the numbers. The function includes docstrings to provide documentation for the function, and includes test cases at the end to verify that the function works correctly.