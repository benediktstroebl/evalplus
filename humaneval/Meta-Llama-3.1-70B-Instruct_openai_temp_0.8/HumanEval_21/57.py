```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of float numbers.

    Returns:
        A list of float numbers rescaled to the range [0, 1].
    """
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    # If all numbers are the same, return a list of zeros (to avoid division by zero)
    if range_value == 0:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_value) / range_value for x in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```