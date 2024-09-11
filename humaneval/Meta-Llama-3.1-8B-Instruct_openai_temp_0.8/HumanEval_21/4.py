```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The input list with the smallest and largest values rescaled to 0 and 1, respectively.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all values in the list are the same
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform to the list
    rescaled_numbers = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines the `rescale_to_unit` function that takes a list of floating point numbers and returns a new list with the same numbers, but with the smallest value in the original list rescaled to 0 and the largest value rescaled to 1. The function uses list comprehension to apply the linear transform to the input list. It also includes a check to ensure that the input list has at least two elements, and a test case at the end to demonstrate its usage.