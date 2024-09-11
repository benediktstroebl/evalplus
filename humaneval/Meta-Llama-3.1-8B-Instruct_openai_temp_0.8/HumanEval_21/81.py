```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: A list of numbers rescaled to the unit interval [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List should have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        raise ValueError("List should have at least two distinct elements")

    rescaled_nums = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_nums

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script includes a function `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers rescaled to the unit interval `[0, 1]`. The function first checks if the input list has at least two elements and that all elements are distinct. It then calculates the minimum and maximum values in the list and uses these values to rescale the numbers. The result is a new list where the smallest number in the original list is 0 and the largest number is 1. The script also includes a test case that demonstrates the function's behavior.