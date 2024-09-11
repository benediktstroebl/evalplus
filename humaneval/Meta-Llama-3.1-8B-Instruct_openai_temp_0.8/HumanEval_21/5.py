```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of numbers

    Returns:
    List[float]: A new list with the transformed numbers

    Raises:
    ValueError: If the input list has less than two elements

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        return [0.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([10.0, 20.0, 30.0]))
print(rescale_to_unit([5.0, 5.0, 5.0]))
try:
    print(rescale_to_unit([5.0]))
except ValueError as e:
    print(e)
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list where each number has been scaled to the range [0, 1]. It handles edge cases such as an empty list or a list with less than two elements, and it includes some example test cases.