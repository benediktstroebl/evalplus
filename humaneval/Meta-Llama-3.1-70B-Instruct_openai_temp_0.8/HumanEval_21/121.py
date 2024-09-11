```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A list of float numbers with the same length as the input, but rescaled to the range [0, 1].
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # If all numbers are the same, return a list of zeros (to avoid division by zero)
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Calculate the range of the numbers
    range_value = max_value - min_value

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(num - min_value) / range_value for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```