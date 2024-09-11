```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of at least two floating point numbers

    Returns:
        A new list where the smallest number from the input list becomes 0 and the largest becomes 1
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        return [1.0] * len(numbers)

    range_num = max_num - min_num

    return [(num - min_num) / range_num for num in numbers]


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```