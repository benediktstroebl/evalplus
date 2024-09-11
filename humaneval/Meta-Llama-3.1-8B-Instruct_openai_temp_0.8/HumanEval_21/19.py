```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): List of floating point numbers

    Returns:
    List[float]: Linearly transformed list of numbers

    Raises:
    ValueError: If the list contains less than two elements

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    
    # Check if all numbers are the same to avoid division by zero error
    if min_num == max_num:
        raise ValueError("All numbers are the same")

    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
transformed_numbers = rescale_to_unit(numbers)
print(transformed_numbers)
```

This code defines a function `rescale_to_unit` that takes a list of floating point numbers, applies a linear transformation to each number, and returns the transformed list. The transformation maps the smallest number in the list to 0 and the largest number to 1. The function raises a `ValueError` if the list contains less than two elements or if all numbers are the same. The example usage demonstrates how to use the function with a sample list of numbers.