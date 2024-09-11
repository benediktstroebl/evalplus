```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    List[float]: The rescaled list of numbers.
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all numbers are the same to avoid division by zero
    if max_val == min_val:
        return [0.0] * len(numbers)

    # Apply the linear transformation
    return [(num - min_val) / (max_val - min_val) for num in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```