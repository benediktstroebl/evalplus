```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: A list of float numbers where the range is [0, 1]

    Raises:
        ValueError: If the list contains less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_value == max_value:
        # If they are the same, return a list of zeros
        return [0.0] * len(numbers)

    # Apply the linear transform
    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers and returns a new list where the range of the original list is mapped to the range [0, 1]. The function first checks if the list contains at least two elements, and if not, raises a `ValueError`. It then finds the minimum and maximum values in the list, applies a linear transform to each number in the list, and returns the result. If the minimum and maximum values are the same, it returns a list of zeros.