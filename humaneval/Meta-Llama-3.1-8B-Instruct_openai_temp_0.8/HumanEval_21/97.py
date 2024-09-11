```python
from typing import List
import math


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of floating point numbers

    Returns:
    List[float]: A list of floating point numbers in the unit range [0, 1]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines a function called `rescale_to_unit` which takes a list of numbers as an argument and returns a new list where the smallest number is 0 and the largest is 1. The script also includes an example usage of the function.

The function works by first checking if the list contains at least two elements. If not, it raises a `ValueError`. It then calculates the minimum and maximum values in the list, and checks if they are the same. If they are, it returns a list of zeros (since there is no range to scale). Otherwise, it uses a list comprehension to create a new list where each number is scaled to the unit range.