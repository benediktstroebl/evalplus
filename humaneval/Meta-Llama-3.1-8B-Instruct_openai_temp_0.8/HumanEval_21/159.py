```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the input list contains less than two elements
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        return [0.0] * len(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Expected output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number is 0 and the largest is 1. It uses a list comprehension to apply a linear transform to each number in the input list. The transform is calculated as `(n - min_num) / (max_num - min_num)`, where `min_num` is the smallest number in the list and `max_num` is the largest. If the list contains less than two elements, it raises a `ValueError`.