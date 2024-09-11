```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: A list of float numbers rescaled to the unit interval [0, 1]

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_val == max_val:
        raise ValueError("The input list must have at least two distinct elements")

    # Apply the linear transformation
    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)
```

This script defines the `rescale_to_unit` function, which takes a list of float numbers as input and returns a new list where the smallest number becomes 0 and the largest becomes 1. It uses list comprehension to apply the linear transformation to each element in the input list. The example usage at the end demonstrates how to use the function and print the result.