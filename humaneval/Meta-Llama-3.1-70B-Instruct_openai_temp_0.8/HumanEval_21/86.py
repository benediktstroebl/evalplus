```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two floating point numbers.

    Returns:
        A list of rescaled numbers between 0 and 1.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value == min_value:
        return [0.0] * len(numbers)

    return [(n - min_value) / (max_value - min_value) for n in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```