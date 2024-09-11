```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are equal to avoid division by zero
    if min_value == max_value:
        return [0.0] * len(numbers)

    rescaled = [(n - min_value) / (max_value - min_value) for n in numbers]

    return rescaled

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number becomes 0 and the largest becomes 1. The function uses a linear transform to achieve this. It also includes input validation to ensure that the list has at least two elements, and it handles the case where all numbers are equal to avoid division by zero. Finally, it includes a test case to demonstrate the function's usage.