```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers (List[float]): A list of floating point numbers with at least two elements.

    Returns:
        List[float]: The input list with its elements rescaled to the unit interval [0, 1].

    Raises:
        ValueError: If the input list has less than two elements.
    """

    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # If all numbers are the same, return a list of zeros (except for the last one, which is 1)
    if min_value == max_value:
        return [0.0] * (len(numbers) - 1) + [1.0]

    # Calculate the range of the input values
    value_range = max_value - min_value

    # Apply the linear transformation to rescale the input values to the unit interval
    rescaled_numbers = [(x - min_value) / value_range for x in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```