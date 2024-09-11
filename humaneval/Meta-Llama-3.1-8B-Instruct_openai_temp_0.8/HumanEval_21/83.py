```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of floating point numbers in the range [0, 1]

    Raises:
        ValueError: If the input list has less than two elements
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all numbers in the list are equal
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply linear transformation
    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input, finds the minimum and maximum values in the list, and applies a linear transformation to each number in the list such that the smallest number becomes 0 and the largest becomes 1. If the input list has less than two elements, the function raises a `ValueError`. The script also includes a test case to demonstrate the function's usage.