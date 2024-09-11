### Rescaling Numbers to Unit Interval

Here is a Python function that rescales a list of numbers to the unit interval [0, 1].

```markdown
### rescale_to_unit.py

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script first checks if the input list contains at least two elements. If not, it raises a ValueError. Then, it calculates the minimum and maximum values in the list. If the minimum and maximum values are equal, it returns a list of zeros. Otherwise, it applies the linear transformation to each number in the list and returns the rescaled list. The script also includes a test case to demonstrate the function's usage.