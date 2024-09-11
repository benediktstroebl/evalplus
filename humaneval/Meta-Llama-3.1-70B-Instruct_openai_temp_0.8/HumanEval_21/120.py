```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The input list with values rescaled to the unit interval [0, 1].

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        return [1.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```