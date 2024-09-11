```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to rescale

    Returns:
        List[float]: A list of rescaled numbers

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

    # Calculate the range of the values
    val_range = max_val - min_val

    # If the range is zero, return a list of zeros
    if val_range == 0:
        return [0.0] * len(numbers)

    # Apply the linear transform to each value in the list
    rescaled_values = [(val - min_val) / val_range for val in numbers]

    return rescaled_values

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been scaled to the range [0, 1]. The function first checks if the input list has at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum values in the list, calculates the range of the values, and applies the linear transform to each value in the list. If the range of the values is zero, it returns a list of zeros. Finally, the script tests the function with a list of numbers and prints the result.