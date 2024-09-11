```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of numbers with at least two elements.

    Returns:
    List[float]: The rescaled list of numbers.

    Raises:
    ValueError: If the input list has less than two elements.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same
    if max_value == min_value:
        return [1.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```