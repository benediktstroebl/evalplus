```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

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

    if max_num == min_num:
        raise ValueError("All numbers in the list are equal")

    return [(n - min_num) / (max_num - min_num) for n in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
print(rescale_to_unit([5.0, 5.0, 5.0]))
print(rescale_to_unit([1.0, 1.0, 1.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number is 0 and the largest number is 1. The function first checks if the list has at least two elements, and if not, it raises a `ValueError`. It then calculates the minimum and maximum numbers in the list, and raises a `ValueError` if all numbers are equal. Finally, it applies a linear transform to each number in the list to rescale it to the unit interval. The transformed list is then returned. The script also includes some test cases to demonstrate the function's behavior.