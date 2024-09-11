```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    
    if max_value == min_value:
        return [0.0] * len(numbers)

    return [(n - min_value) / (max_value - min_value) for n in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines a function `rescale_to_unit` that takes a list of floats as input and returns a new list with the same numbers, but linearly transformed so that the smallest number becomes 0 and the largest becomes 1. The script includes type hints for the function parameters and return type, as well as a docstring to explain what the function does. The script also includes a test case at the end to demonstrate the function's behavior.