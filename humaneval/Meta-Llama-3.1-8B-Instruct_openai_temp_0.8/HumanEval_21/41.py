```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of at least two float elements

    Returns:
    List[float]: A list of float elements with the same relative order as the input list,
                 but with the smallest number becoming 0 and the largest number becoming 1

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    if min_num == max_num:
        return [0.0] * len(numbers)

    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and applies a linear transformation to them, such that the smallest number becomes 0 and the largest number becomes 1. The function uses list comprehension to apply the transformation to each number in the input list. It also includes a docstring that describes what the function does, what arguments it takes, and what it returns, as well as an example usage of the function.