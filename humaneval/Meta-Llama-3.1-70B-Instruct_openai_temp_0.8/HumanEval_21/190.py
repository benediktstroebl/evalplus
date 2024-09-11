```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The transformed list of numbers.

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    # Check for div by zero
    if max_num == min_num:
        return [1.0] * len(numbers)

    return [(num - min_num) / (max_num - min_num) for num in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of floating point numbers and applies a linear transformation to it, such that the smallest number becomes 0 and the largest becomes 1. It checks for the edge case where the input list has less than two elements and raises a `ValueError` if that's the case. It also checks for division by zero and returns a list of ones in that case. The function uses list comprehension to create the transformed list. Finally, it includes an example usage of the function.