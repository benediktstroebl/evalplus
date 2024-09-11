### Rescaling a List of Numbers to Unit Range
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

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("list must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```
This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input and returns a new list where the smallest number is 0 and the largest is 1. The function first checks if the input list contains at least two elements, and if not, raises a `ValueError`. It then calculates the minimum and maximum values in the list, and applies a linear transform to each number in the list by subtracting the minimum value and dividing by the range of the data (i.e., the difference between the maximum and minimum values). If the maximum and minimum values are the same, the function returns a list of zeros. The example usage at the end shows how to use the `rescale_to_unit` function with a sample list of numbers.