```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floats

    Returns:
        A list of floats where the smallest number is 0 and the largest is 1

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value - min_value == 0:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that rescales a list of numbers to the range [0, 1]. It checks if the list has at least two elements, and if not, raises a ValueError. It also checks for division by zero and handles that case by returning a list of zeros. The rescaling is done using a list comprehension, which is a concise way to create a new list by applying a transformation to each element of the original list. The script includes a test case to demonstrate the function's behavior.