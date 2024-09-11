```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of floating point numbers.

    Returns:
        A new list of floating point numbers, rescaled to the unit range [0, 1].

    Raises:
        ValueError: If the input list has less than two elements.
    """

    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Calculate the range of the values
    val_range = max_val - min_val

    # If all values are the same, return a list of zeros
    if val_range == 0:
        return [0.0] * len(numbers)

    # Apply the linear transform to each value in the list
    rescaled_numbers = [(x - min_val) / val_range for x in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```