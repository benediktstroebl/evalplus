```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of at least two float numbers

    Returns:
    List[float]: The rescaled list of numbers

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    if min_num == max_num:
        # If all numbers are the same, return a list of zeros
        return [0.0] * len(numbers)

    return [(x - min_num) / (max_num - min_num) for x in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers rescaled to be between 0 and 1. The rescaling is done by subtracting the smallest number in the list and then dividing by the difference between the smallest and largest numbers.

The function first checks if the list contains at least two elements, raising a `ValueError` if it does not. If all numbers in the list are the same, it returns a list of zeros. Otherwise, it uses a list comprehension to apply the rescaling to each number in the list.

The script includes a test case to demonstrate how to use the function.