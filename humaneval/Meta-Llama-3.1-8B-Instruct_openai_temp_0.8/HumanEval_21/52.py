### Rescale a List of Numbers to Unit Interval

```markdown
# rescale_to_unit.py

from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the smallest number is mapped to 0 and the largest number is mapped to 1. The script also includes example usage and checks for the case when the input list has fewer than two elements.