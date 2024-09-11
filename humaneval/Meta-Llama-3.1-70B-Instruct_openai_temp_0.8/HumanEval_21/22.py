```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of float numbers.

    Returns:
        A list of float numbers where the smallest number is 0 and the largest is 1.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        return [0.0] * len(numbers)

    return [(num - min_num) / (max_num - min_num) for num in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script applies a linear transformation to the input list of numbers. The transformation is such that the smallest number becomes 0 and the largest becomes 1. If the input list contains less than two elements, a ValueError is raised. If all numbers in the list are the same, the function returns a list of zeros.