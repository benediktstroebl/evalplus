```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of at least two float numbers

    Returns:
        A list of float numbers representing the rescaled list

    Raises:
        ValueError: If the input list contains less than two numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")

    min_num = min(numbers)
    max_num = max(numbers)

    # Check for division by zero
    if max_num == min_num:
        raise ValueError("All numbers in the list are equal")

    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers, applies a linear transform to rescale the list to the range [0, 1], and returns the result. The function raises a `ValueError` if the input list contains less than two numbers or if all numbers in the list are equal. The example usage at the end demonstrates how to use the function with a list of numbers.