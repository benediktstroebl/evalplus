```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of floating point numbers rescaled to the unit interval

    Raises:
        ValueError: If the input list has less than 2 elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value - min_value == 0:
        raise ValueError("All numbers in the list are equal")

    return [(num - min_value) / (max_value - min_value) for num in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script first checks if the input list has at least two elements. If not, it raises a ValueError. Then, it calculates the minimum and maximum values in the list. It checks if all numbers are equal, and if so, raises a ValueError because division by zero would occur. Otherwise, it applies a linear transformation to each number in the list, mapping the smallest number to 0 and the largest number to 1.