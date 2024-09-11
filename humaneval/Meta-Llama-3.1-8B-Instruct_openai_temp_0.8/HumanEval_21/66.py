```python
from typing import List

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
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All elements in the list are the same")

    # Apply the linear transform
    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled_numbers

# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of floats as input and returns a new list with the same numbers scaled to be between 0 and 1. It first checks if the input list has at least two elements and if all elements are the same (in which case division by zero occurs). It then applies the linear transform to each number in the list, subtracting the minimum value and dividing by the range of the input list. The result is a list of floats between 0 and 1. The script also includes an example usage of the function.