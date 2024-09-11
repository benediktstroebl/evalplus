```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers: A list of floats with at least two elements.

    Returns:
    A list of floats where the smallest number is 0 and the largest is 1.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all numbers are the same to avoid division by zero
    if max_val == min_val:
        return [0.0] * len(numbers)

    # Apply linear transformation
    scaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    return scaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```