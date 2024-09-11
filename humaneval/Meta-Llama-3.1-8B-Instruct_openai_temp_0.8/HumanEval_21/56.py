```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to be rescaled

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the list contains less than two numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")

    min_num = min(numbers)
    max_num = max(numbers)

    # Check if all numbers are identical
    if min_num == max_num:
        return [0.0] * len(numbers)

    rescaled = [(num - min_num) / (max_num - min_num) for num in numbers]
    return rescaled

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number is mapped to 0 and the largest is mapped to 1. The function first checks if the input list contains fewer than two numbers and raises a `ValueError` if so. It then computes the minimum and maximum values in the list. If all numbers are identical, the function returns a list of zeros. Otherwise, it uses a list comprehension to rescale each number by subtracting the minimum and dividing by the range of the original list. The rescaled numbers are then returned as a list.