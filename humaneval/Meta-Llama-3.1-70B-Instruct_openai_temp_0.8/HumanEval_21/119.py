```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
    numbers: A list of floating point numbers.

    Returns:
    A new list where the smallest number from the input list is mapped to 0.0 and the largest is mapped to 1.0.
    All other numbers are linearly interpolated between 0.0 and 1.0.

    Raises:
    ValueError: If the input list contains less than two elements.
    """

    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    # If all numbers are equal, return a list with all 0.0
    if range_value == 0.0:
        return [0.0] * len(numbers)

    return [(x - min_value) / range_value for x in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```