### Linear Rescaling of a List of Numbers
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: A list of float numbers rescaled to the unit interval [0, 1]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        raise ValueError("All numbers in the list must be distinct")

    # Apply linear transform to rescale numbers to the unit interval [0, 1]
    return [(x - min_num) / (max_num - min_num) for x in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers as input and returns a new list with the same numbers rescaled to the unit interval [0, 1]. The function first checks if the input list contains at least two distinct numbers. If not, it raises a `ValueError`. Then it applies a linear transform to each number in the list by subtracting the minimum number and dividing by the range (maximum minus minimum) of the input list. The result is a new list with the same numbers rescaled to the unit interval [0, 1].