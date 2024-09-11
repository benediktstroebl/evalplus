```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to the given list of numbers, 
    such that the smallest number will become 0 and the largest will become 1.

    Args:
    numbers (List[float]): A list of at least two elements.

    Returns:
    List[float]: The rescaled list of numbers.

    Examples:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_value == max_value:
        raise ValueError("All numbers in the list are the same.")

    # Calculate the rescaled values
    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return rescaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input and returns a list of rescaled floating point numbers. The rescaling is done such that the smallest number in the input list becomes 0 and the largest becomes 1. The function includes error checking to ensure that the input list has at least two elements and that the minimum and maximum values in the list are not the same.