```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        raise ValueError("All numbers in the list must be different")

    rescaled = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been scaled to the range [0, 1]. The scaling is linear, so that the smallest number in the original list will become 0 and the largest will become 1. The function also includes error checking to ensure that the input list contains at least two elements and that all numbers in the list are different.