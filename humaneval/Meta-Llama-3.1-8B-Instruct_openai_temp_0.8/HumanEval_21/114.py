```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the list has less than two elements.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        return [0.0] * len(numbers)

    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

This script defines a function `rescale_to_unit` that takes a list of numbers, rescales it to the range [0, 1], and returns the result. It also handles edge cases where the list has less than two elements or all elements are equal. The example usage at the end demonstrates how to use the function.