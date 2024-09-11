```markdown
### Rescale Numbers to Unit Interval
#### Problem Description
Given a list of numbers, apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.

#### Solution

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescale a list of numbers to the unit interval [0, 1].

    Args:
    numbers (List[float]): A list of at least two numbers.

    Returns:
    List[float]: The rescaled list.

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns the list with each number transformed to the unit interval [0, 1]. The transformation is achieved by subtracting the minimum value in the list and then dividing by the range of the list (i.e., the difference between the maximum and minimum values). The result is a list where the smallest number becomes 0 and the largest becomes 1. The script also includes an example usage of the function.