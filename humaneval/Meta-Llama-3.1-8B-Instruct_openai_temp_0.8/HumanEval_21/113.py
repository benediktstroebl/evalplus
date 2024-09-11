```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        return [0.0] * len(numbers)

    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # [0.0, 0.0, 0.0, 0.0, 0.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the values are rescaled to be between 0 and 1. If the list contains less than two elements, it raises a `ValueError`. If the list contains a single element or all elements are the same, it returns a list of zeros. Otherwise, it uses a linear transformation to map the smallest number to 0 and the largest number to 1. Finally, it tests the function with a few examples.