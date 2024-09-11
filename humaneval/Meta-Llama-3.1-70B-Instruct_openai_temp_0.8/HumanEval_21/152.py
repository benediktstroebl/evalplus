```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floats with at least two elements

    Returns:
        A list of floats where the smallest number is 0 and the largest is 1
    """
    # Check that the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        return [1.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # [1.0, 1.0, 1.0, 1.0, 1.0]
print(rescale_to_unit([1.1, 2.2, 3.3, 4.4, 5.5]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([-1.0, 0.0, 1.0, 2.0, 3.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```