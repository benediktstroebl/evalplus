```markdown
### Rescaling a List of Numbers to Unit Interval

The following Python function `rescale_to_unit` takes a list of numbers and rescales it to a unit interval, where the smallest number becomes 0 and the largest becomes 1.

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floating point numbers

    Returns:
        A list of floating point numbers rescaled to the unit interval

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    if max_value == min_value:
        return [0.0] * len(numbers)

    rescaled_values = [(n - min_value) / (max_value - min_value) for n in numbers]
    return rescaled_values

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

This script first checks if the list contains at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum values in the list. If the maximum and minimum values are the same, it returns a list of zeros. Otherwise, it applies a linear rescaling transform to each number in the list, where each number `n` is rescaled to `(n - min_value) / (max_value - min_value)`. The rescaled list is then returned.