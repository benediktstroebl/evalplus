### Rescaling List of Numbers to Unit Interval

Below is a Python script that defines the `rescale_to_unit` function, which applies a linear transformation to a list of numbers, mapping the smallest number to 0 and the largest to 1:

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The rescaled list of numbers

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Apply the linear transformation
    # This is done using the formula: (x - min_val) / (max_val - min_val)
    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script first checks if the input list contains at least two elements, raising a `ValueError` if not. Then, it finds the minimum and maximum values in the list using the built-in `min` and `max` functions. Finally, it applies the linear transformation to each element in the list using a list comprehension and returns the rescaled list.