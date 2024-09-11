```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two floating point numbers.

    Returns:
        A list of rescaled numbers between 0 and 1.

    Raises:
        ValueError: If the input list contains less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    range_value = max_value - min_value

    # Handle the case where all numbers are the same
    if range_value == 0:
        return [1.0] * len(numbers)

    rescaled_numbers = [(n - min_value) / range_value for n in numbers]
    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function, which takes a list of floating point numbers as input, 
applies a linear transformation to rescale the numbers between 0 and 1, 
and returns the rescaled list. The function includes input validation to ensure the list contains at least two elements. 
The example usage demonstrates how to call the function with a sample list of numbers and print the rescaled result.