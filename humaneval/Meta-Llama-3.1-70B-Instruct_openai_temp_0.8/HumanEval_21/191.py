```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: The rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num

    if range_num == 0:
        return [1.0] * len(numbers)  # If all numbers are the same, return a list of 1.0

    return [(num - min_num) / range_num for num in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers, but rescaled so that the smallest number becomes 0 and the largest becomes 1. The function uses list comprehension to create the new list. If all numbers in the input list are the same, the function returns a list of 1.0.