### Rescale a List of Numbers to Unit Interval

The following Python script defines a function `rescale_to_unit` to transform a list of numbers into a unit interval from 0 to 1.

```python
from typing import List
import math

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of float numbers

    Returns:
    List[float]: The list of rescaled numbers

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Find the min and max values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines the `rescale_to_unit` function, which takes a list of numbers as input, finds the minimum and maximum values, and then applies a linear transform to each number in the list to rescale it to the unit interval from 0 to 1. The function also includes error handling to ensure the input list has at least two elements. The example usage demonstrates how to use the function with a sample list of numbers.