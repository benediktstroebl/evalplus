```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: The rescaled list of numbers.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [1.0] * len(numbers)

    range_val = max_val - min_val
    return [(x - min_val) / range_val for x in numbers]


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([-1.0, 0.0, 1.0]))  # Output: [0.0, 0.5, 1.0]
print(rescale_to_unit([10.0, 10.0, 10.0]))  # Output: [1.0, 1.0, 1.0]
```