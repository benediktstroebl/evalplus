```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value == min_value:
        raise ValueError("All elements in the list are the same")

    # Apply the linear transform
    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return rescaled_numbers

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers, finds the minimum and maximum values in the list, and then applies a linear transform to the list such that the smallest number becomes 0 and the largest becomes 1. The function returns the rescaled list of numbers. The script also includes example usage and error checking for cases where the list contains less than two elements or all elements are the same.