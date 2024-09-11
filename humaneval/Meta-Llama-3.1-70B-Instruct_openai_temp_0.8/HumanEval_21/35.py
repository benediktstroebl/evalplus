```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: A list of numbers rescaled to the unit interval [0, 1].
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        return [1.0] * len(numbers)  # all numbers are the same, return 1.0 for all

    # Calculate the scaling factor
    scale = 1 / (max_value - min_value)

    # Apply the linear transformation
    rescaled_numbers = [(num - min_value) * scale for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```