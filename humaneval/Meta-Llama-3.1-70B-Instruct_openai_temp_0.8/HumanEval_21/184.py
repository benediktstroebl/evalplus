```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    List[float]: The input list with its values rescaled between 0 and 1.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # Check for division by zero
    if value_range == 0:
        # If all values are the same, return a list of zeros (except for the last one which is 1)
        return [0.0] * (len(numbers) - 1) + [1.0]

    # Apply the linear transformation
    rescaled_numbers = [(n - min_value) / value_range for n in numbers]

    return rescaled_numbers


# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```