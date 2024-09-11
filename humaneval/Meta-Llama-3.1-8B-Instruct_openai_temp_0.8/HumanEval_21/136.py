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

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where each number has been rescaled to be between 0 and 1. The rescaling is done using a linear transform, where the smallest number in the input list becomes 0 and the largest becomes 1.

The function first checks if the input list has at least two elements. If not, it raises a `ValueError`. If the list has only one element, the function returns a list with all elements equal to 0.

The rescaling is done by subtracting the smallest value in the list from each number and then dividing by the difference between the largest and smallest values in the list. This ensures that the smallest number becomes 0 and the largest becomes 1.

The script also includes a test case to demonstrate the function's behavior.