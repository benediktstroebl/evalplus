```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    rescaling them to the range [0, 1], 
    where the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of floating point numbers with at least two elements.

    Returns:
        A new list of floating point numbers, where the smallest input number is 0 and the largest is 1.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    if range_value == 0:
        return [1.0] * len(numbers)

    return [(n - min_value) / range_value for n in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```