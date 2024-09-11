```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two floating point numbers

    Returns:
        List[float]: A list of scaled numbers between 0 and 1

    Raises:
        ValueError: If the input list has less than two elements.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(num - min_val) / (max_val - min_val) for num in numbers]

# Testing the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This Python script defines a function `rescale_to_unit` that takes a list of floating point numbers as input and returns a new list where each number is scaled to be between 0 and 1, inclusive. The scaling is done in a way that the smallest number in the input list becomes 0 and the largest number becomes 1. The function also includes error checking to ensure that the input list has at least two elements.