```markdown
### Rescaling a List of Numbers to the Unit Interval
#### A Python Script

This script provides a function `rescale_to_unit` that takes a list of numbers and applies a linear transformation to scale the numbers to the unit interval [0, 1].

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating-point numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers in the list are the same
    if max_value == min_value:
        raise ValueError("All numbers in the list must be different")

    # Apply the linear transformation to rescale the numbers to the unit interval
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script uses a list comprehension to apply the linear transformation to each number in the input list. The transformation is calculated as `(x - min_value) / (max_value - min_value)`, where `x` is the current number, `min_value` is the smallest number in the list, and `max_value` is the largest number in the list. The resulting rescaled numbers are returned as a list.