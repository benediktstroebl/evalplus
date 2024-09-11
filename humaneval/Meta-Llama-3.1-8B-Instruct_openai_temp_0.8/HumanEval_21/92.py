Here's a Python script that implements the `rescale_to_unit` function as specified:
```markdown
### Rescale Numbers to Unit Range
#### Solution: Linear Transformation

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): List of numbers to rescale.

    Returns:
        List[float]: Rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.0] * len(numbers)  # All elements are the same, return a list of zeros

    return [(x - min_val) / range_val for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines the `rescale_to_unit` function, which takes a list of numbers as input and returns a new list where each number has been linearly transformed to the range [0, 1]. The function first checks if the input list has at least two elements, and raises a `ValueError` if not. It then calculates the minimum and maximum values in the list, and applies the transformation to each element. If all elements in the list are the same, it returns a list of zeros.