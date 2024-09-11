```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floating point numbers

    Returns:
        A list of floating point numbers, rescaled to the unit interval [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        return [0.0] * len(numbers)

    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list with the same numbers, but rescaled to the unit interval [0, 1]. The script also includes a test case to demonstrate the function's behavior. The function works by first finding the minimum and maximum values in the input list, then applying a linear transform to each number in the list to map it to the unit interval. If the input list has less than two elements, the function raises a `ValueError`. If the minimum and maximum values in the input list are equal, the function returns a list of zeros.