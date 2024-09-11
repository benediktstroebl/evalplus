```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to a list of numbers, scaling the smallest number to 0 and the largest to 1.

    Args:
        numbers: A list of floating point numbers with at least two elements.

    Returns:
        A new list with the numbers rescaled to the unit interval [0, 1].
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        return [1.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([-10.0, 0.0, 10.0]))  # Output: [0.0, 0.5, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0]))  # Output: [1.0, 1.0, 1.0]
```