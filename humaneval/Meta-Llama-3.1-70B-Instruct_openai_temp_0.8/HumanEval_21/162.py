```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Apply a linear transform to the input list of numbers, such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: The input list with all numbers rescaled to the range [0, 1].

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value == min_value:
        return [1.0] * len(numbers)

    range_value = max_value - min_value
    return [(x - min_value) / range_value for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```