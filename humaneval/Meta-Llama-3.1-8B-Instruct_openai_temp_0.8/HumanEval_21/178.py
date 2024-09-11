### Linear Transformation to Unit Interval
#### Rescale a list of numbers to the unit interval [0, 1]

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of at least two float numbers

    Returns:
        A list of rescaled float numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        # handle the case where all numbers are the same
        return [0.0]*len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

Note that this implementation includes input validation to ensure the list has at least two elements. If the list has duplicate values, these are handled by returning a list with the same repeated values (i.e., `[0.0]*len(numbers)`) to maintain the original length.