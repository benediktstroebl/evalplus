```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)

    # Avoid division by zero
    if max_value == min_value:
        return [0.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input, applies a linear transformation to scale the numbers to the range [0, 1], and returns the rescaled list. The function first checks if the input list has at least two elements and raises a `ValueError` if not. It then finds the minimum and maximum values in the list and uses them to calculate the rescaled values. The function also handles the case where the minimum and maximum values are equal to avoid division by zero.