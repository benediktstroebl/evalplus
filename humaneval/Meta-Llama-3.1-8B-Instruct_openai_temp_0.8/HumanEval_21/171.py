### Rescaling to Unit Range

Here's a Python script that implements the `rescale_to_unit` function:

```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of float numbers

    Returns:
        A new list of float numbers rescaled to the unit range [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if min_value == max_value:
        return [0.0] * len(numbers)

    rescaled_numbers = [(n - min_value) / (max_value - min_value) for n in numbers]
    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script first checks if the input list has at least two elements. If not, it raises a `ValueError`. Then, it calculates the minimum and maximum values in the list. If the minimum and maximum values are the same, the function returns a list of zeros, since all numbers are identical.

Finally, the script applies the linear transformation to rescale the numbers to the unit range [0, 1]. It uses a list comprehension to create a new list with the rescaled numbers.