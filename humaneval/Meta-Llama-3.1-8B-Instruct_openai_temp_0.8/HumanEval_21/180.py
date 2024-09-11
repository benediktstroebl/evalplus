### Rescaling Numbers to Unit Range

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to rescale

    Returns:
        List[float]: Rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    return [(num - min_value) / (max_value - min_value) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been rescaled to the range [0, 1]. The rescaling is done by subtracting the minimum value from each number and then dividing by the range of the input numbers. This function raises a `ValueError` if the input list contains less than two elements, since rescaling is not possible in this case.