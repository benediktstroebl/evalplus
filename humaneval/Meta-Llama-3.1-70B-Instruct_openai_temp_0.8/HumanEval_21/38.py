```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    rescaling the smallest number to 0 and the largest to 1.

    Args:
        numbers: A list of floats with at least two elements.

    Returns:
        A new list with the same length as the input, but with values rescaled.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    # Avoid division by zero if all numbers are the same
    if max_val == min_val:
        return [0.0] * len(numbers)

    range_val = max_val - min_val
    return [(num - min_val) / range_val for num in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```