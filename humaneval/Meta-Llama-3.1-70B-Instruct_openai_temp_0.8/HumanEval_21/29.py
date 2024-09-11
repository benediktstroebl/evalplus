```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    rescaling the smallest number to 0 and the largest to 1.

    Args:
    numbers: A list of at least two float numbers.

    Returns:
    A list of rescaled float numbers.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list should have at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same to avoid division by zero
    if max_value == min_value:
        return [1.0] * len(numbers)

    # Calculate the range of the numbers
    range_value = max_value - min_value

    # Apply the linear transformation to each number
    rescaled_numbers = [(num - min_value) / range_value for num in numbers]

    return rescaled_numbers


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # [1.0, 1.0, 1.0, 1.0, 1.0]
```