```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers: A list of float numbers (at least two elements)

    Returns:
    A list of float numbers where the smallest number is 0 and the largest is 1
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [1.0] * len(numbers)  # Handle the case where all numbers are the same

    range_val = max_val - min_val

    return [(x - min_val) / range_val for x in numbers]

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```