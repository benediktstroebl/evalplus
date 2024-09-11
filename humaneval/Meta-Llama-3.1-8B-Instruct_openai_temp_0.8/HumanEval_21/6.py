```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers, apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        raise ValueError("List must contain at least two distinct elements")

    scale = 1 / (max_value - min_value)
    shifted_numbers = [n - min_value for n in numbers]

    rescaled_numbers = [s * scale for s in shifted_numbers]

    return rescaled_numbers

# Testing the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```
In this script, the function `rescale_to_unit` takes a list of numbers, shifts them to start at 0, scales them to have a range of 1, and returns the resulting list. The script includes a docstring that provides documentation for the function, including its parameters, return value, and an example usage. It also includes a test case to demonstrate the function's behavior.