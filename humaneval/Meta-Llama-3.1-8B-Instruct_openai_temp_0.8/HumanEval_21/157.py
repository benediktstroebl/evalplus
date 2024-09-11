```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of float numbers

    Returns:
    List[float]: The rescaled list of numbers

    Raises:
    ValueError: If the input list has less than two elements

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if the minimum and maximum values are equal (i.e., all numbers are the same)
    if min_val == max_val:
        raise ValueError("All numbers in the list are the same")

    # Apply the linear transform
    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled_numbers

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([10.0, 20.0, 30.0]))  # Output: [0.0, 0.5, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number becomes 0 and the largest becomes 1. The function uses list comprehension to apply the linear transform to each number in the input list. It also includes error checking to ensure that the input list has at least two elements and that not all numbers in the list are the same.