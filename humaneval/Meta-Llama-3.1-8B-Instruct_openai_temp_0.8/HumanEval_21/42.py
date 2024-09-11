```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers

    Returns:
        List[float]: List of numbers rescaled to the unit interval

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    # Check for division by zero condition
    if max_num == min_num:
        raise ValueError("All numbers in the list are equal")

    return [(x - min_num) / (max_num - min_num) for x in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers, but scaled to the unit interval [0, 1]. The function first checks that the input list has at least two elements, and that all elements are not equal (to avoid division by zero). It then uses list comprehension to apply the linear transformation to each number in the list. The test at the end of the script demonstrates how to use the function.