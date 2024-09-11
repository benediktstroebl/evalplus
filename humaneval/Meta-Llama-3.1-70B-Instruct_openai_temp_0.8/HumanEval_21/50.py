```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The input list scaled to the unit interval [0, 1].
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    # Handle the case where all numbers are equal to avoid division by zero
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    scaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return scaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
scaled_numbers = rescale_to_unit(numbers)
print(scaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```