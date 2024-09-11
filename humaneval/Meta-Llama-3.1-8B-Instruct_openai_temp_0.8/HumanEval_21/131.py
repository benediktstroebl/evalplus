```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers.

    Returns:
        List[float]: A list of float numbers scaled to the unit range [0, 1].

    Raises:
        ValueError: If the input list has less than two elements.

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        return [0.0] * len(numbers)

    return [(n - min_value) / (max_value - min_value) for n in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
scaled_numbers = rescale_to_unit(numbers)
print(scaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers and returns a new list with the same numbers scaled to the range [0, 1]. It first checks if the input list has at least two elements, and raises a `ValueError` if not. It then finds the minimum and maximum values in the list, and uses these to scale the numbers. If the minimum and maximum values are the same, it returns a list of zeros. Finally, it uses a list comprehension to scale each number in the input list and returns the resulting list. The example usage at the end demonstrates how to use the function with a sample list of numbers.