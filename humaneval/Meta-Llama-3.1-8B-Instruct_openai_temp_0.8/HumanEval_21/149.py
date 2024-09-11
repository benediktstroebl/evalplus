```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The input list of numbers rescaled to the unit interval [0, 1]

    Raises:
        ValueError: If the input list has less than two elements

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All elements in the list must be distinct")

    return [(num - min_val) / (max_val - min_val) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input and returns a new list with the same elements, but rescaled to the unit interval [0, 1]. The function first checks if the input list has at least two elements, and if all elements are distinct. It then calculates the minimum and maximum values in the list, and applies a linear transformation to each element in the list, mapping the smallest value to 0 and the largest value to 1. The result is a new list with the same number of elements, but with values in the unit interval.