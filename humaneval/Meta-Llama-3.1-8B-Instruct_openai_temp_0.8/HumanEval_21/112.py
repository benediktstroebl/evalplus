```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two float elements

    Returns:
        List[float]: The input list rescaled to the unit interval

    Raises:
        ValueError: If the input list contains less than two elements
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero (i.e., a list with all elements equal)
    if max_val == min_val:
        return [0.0] * len(numbers)

    # Apply the linear transform
    return [(num - min_val) / (max_val - min_val) for num in numbers]

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers and returns a new list where each element has been linearly transformed to be between 0 and 1. The transformation is done by subtracting the minimum value in the list from each element and then dividing by the range of the list (i.e., the difference between the maximum and minimum values). The script also includes a docstring that explains the function's purpose, arguments, return value, and any potential exceptions it raises.