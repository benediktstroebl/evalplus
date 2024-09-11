Here's a Python script that solves the problem in a self-contained markdown code block:

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of numbers to rescale.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if max_val == min_val:
        raise ValueError("All elements in the list must be different")

    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]
    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This Python script defines a function `rescale_to_unit` that takes a list of numbers as input and returns the rescaled list. The function first checks if the input list contains at least two elements and if all elements are different. Then it calculates the minimum and maximum values in the list and applies a linear transformation to each number in the list, scaling the smallest number to 0 and the largest number to 1. The rescaled numbers are stored in a new list and returned by the function.