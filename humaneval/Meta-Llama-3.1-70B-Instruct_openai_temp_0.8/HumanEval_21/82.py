```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of numbers with at least two elements.

    Returns:
        A list of numbers where the smallest number is 0 and the largest number is 1.

    Raises:
        ValueError: If the list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        # If all numbers are the same, return a list of zeros
        return [0.0] * len(numbers)

    range_value = max_value - min_value

    return [(n - min_value) / range_value for n in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```