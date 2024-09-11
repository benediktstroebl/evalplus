```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of numbers in the range [0, 1]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for degenerate cases where all numbers are the same
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform to the list
    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and applies a linear transform to the list, such that the smallest number becomes 0 and the largest number becomes 1. The function also includes input validation to ensure the list contains at least two elements. The script includes a test case to demonstrate the function's behavior.