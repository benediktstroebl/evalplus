```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floating point numbers

    Returns:
        A list of floating point numbers with the same relative distances as the input,
        but scaled to the range [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        return [0.0] * len(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same relative distances, but scaled to the range [0, 1]. It first checks if the list contains at least two elements and raises an error if not. Then it calculates the minimum and maximum values in the list. If the minimum and maximum values are the same, it returns a list of zeros, because there is no scaling to be done. Otherwise, it applies a linear transformation to each number in the list, subtracting the minimum value and dividing by the range, to get a new list where the smallest number is 0 and the largest is 1.