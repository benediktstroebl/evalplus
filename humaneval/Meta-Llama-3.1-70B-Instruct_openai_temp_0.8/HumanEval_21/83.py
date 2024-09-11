```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    List[float]: The input list rescaled to the unit range [0, 1].
    """
    # Check if the list contains less than two elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same (to avoid division by zero)
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation to the list
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input, applies a linear transformation to the list, and returns the rescaled list. The linear transformation maps the smallest number in the list to 0 and the largest number to 1. The function includes error checking to handle cases where the input list contains less than two elements or all numbers are the same. The script also includes an example usage of the function.