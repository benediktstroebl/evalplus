```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

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

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([-1.0, 0.0, 1.0]))
print(rescale_to_unit([1.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been rescaled to the range [0, 1]. The smallest number in the input list becomes 0 and the largest number becomes 1. If the input list has less than two elements, a ValueError is raised. The script also includes test cases to demonstrate the function's behavior.