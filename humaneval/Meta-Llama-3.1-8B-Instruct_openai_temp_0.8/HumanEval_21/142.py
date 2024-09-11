```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two floating point numbers

    Returns:
        List[float]: The list of numbers rescaled to the unit interval [0, 1]
    """
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all numbers in the list are equal
    if min_val == max_val:
        raise ValueError("All numbers in the list must be different")

    # Apply the linear transform
    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function which takes a list of numbers and returns a new list with the same numbers rescaled to the unit interval [0, 1]. The function first checks if the input list has at least two elements, and if not, it raises a `ValueError`. It then finds the minimum and maximum values in the list, applies a linear transform to the numbers in the list using these values, and returns the resulting list. If all numbers in the list are equal, the function also raises a `ValueError`.