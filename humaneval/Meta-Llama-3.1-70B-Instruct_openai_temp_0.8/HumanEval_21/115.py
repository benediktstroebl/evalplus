```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)

    # If all numbers are the same, return a list with all zeros except the last one which is 1
    if min_value == max_value:
        return [0.0] * (len(numbers) - 1) + [1.0]

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list with the same numbers rescaled to the range [0, 1]. The function first checks if the list has at least two elements, then finds the minimum and maximum values in the list. If all numbers are the same, it returns a list with all zeros except the last one which is 1. Otherwise, it uses a list comprehension to apply the linear transformation to each number in the list. The transformation subtracts the minimum value from each number and then divides by the range of the numbers.