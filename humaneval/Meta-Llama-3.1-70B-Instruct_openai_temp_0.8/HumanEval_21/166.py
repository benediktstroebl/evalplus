```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to the input list of numbers, such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: The rescaled list of numbers.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for the case where all numbers are equal (to avoid division by zero)
    if max_value == min_value:
        return [0.0] * len(numbers)

    # Apply the linear transform to the list
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # Output: [0.0, 0.0, 0.0, 0.0, 0.0]
```