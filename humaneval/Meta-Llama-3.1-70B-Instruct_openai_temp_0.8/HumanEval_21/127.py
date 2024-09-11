```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of numbers with at least two elements.

    Returns:
        List[float]: The input list with all numbers rescaled to the unit interval [0, 1].
    """
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Calculate the range of the input list
    range_value = max_value - min_value

    # Check if the range is zero to avoid division by zero
    if range_value == 0:
        return [1.0] * len(numbers)

    # Apply the linear transformation to the input list
    rescaled_numbers = [(x - min_value) / range_value for x in numbers]

    return rescaled_numbers


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```