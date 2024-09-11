```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of floating point numbers.

    Returns:
        A new list of floating point numbers, where the smallest number is 0 and the largest is 1.

    Raises:
        ValueError: If the input list contains less than two elements.
    """

    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must contain at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # If all values are the same, return a list of zeros (to avoid division by zero)
    if value_range == 0:
        return [0.0] * len(numbers)

    # Apply the linear transformation to each value
    return [(value - min_value) / value_range for value in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```