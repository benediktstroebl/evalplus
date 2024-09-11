```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of floats with at least two elements.

    Returns:
        The input list rescaled to the unit interval [0, 1].

    Raises:
        ValueError: If the input list has less than two elements.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # [0.0, 0.0, 0.0, 0.0, 0.0]
print(rescale_to_unit([-2.0, 0.0, 2.0, 4.0, 6.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```