```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): The list of numbers to rescale

    Returns:
        List[float]: The rescaled list of numbers

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list of numbers must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All numbers in the list are equal")

    return [(num - min_val) / (max_val - min_val) for num in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script includes a check to ensure the input list has at least two elements, and another check to prevent division by zero in case all numbers are equal. It then uses list comprehension to apply the linear transformation to the input list.