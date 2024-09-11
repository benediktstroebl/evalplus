```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of floating point numbers

    Returns:
    List[float]: A list of floating point numbers scaled between 0 and 1
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("List must have unique elements")

    # Apply the linear transform
    scaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    return scaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines the `rescale_to_unit` function, which takes a list of numbers as input and returns a list of the same numbers, scaled between 0 and 1. It uses list comprehension to apply the linear transform to each number in the list. The test at the end demonstrates the function's usage.