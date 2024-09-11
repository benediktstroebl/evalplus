```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of numbers in the range [0, 1]

    Raises:
        ValueError: If the list has less than two elements

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        raise ValueError("All numbers in the list must be different")

    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([0.0, 10.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers, applies a linear transform to rescale them to the range [0, 1], and returns the resulting list. The transform is defined as `(num - min_num) / (max_num - min_num)`, where `num` is each number in the list, `min_num` is the smallest number in the list, and `max_num` is the largest number in the list.

The script includes a docstring that describes the function's behavior, its parameters, its return value, and the exceptions it raises. It also includes some test cases to demonstrate the function's behavior.