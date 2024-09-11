Here's a self-contained Python script that solves the problem:
```markdown
### Rescale List of Numbers to Unit Range

This script defines a function `rescale_to_unit` that applies a linear transform to a list of numbers,
such that the smallest number becomes 0 and the largest becomes 1.
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two floating point numbers

    Returns:
        List[float]: The list of numbers rescaled to the unit range [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)
    return [(n - min_value) / (max_value - min_value) for n in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
In this script, the `rescale_to_unit` function first checks if the input list has at least two elements. If not, it raises a `ValueError`. Then it calculates the minimum and maximum values in the list. Finally, it applies the linear transform to each number in the list, subtracting the minimum value and dividing by the range (i.e., the maximum value minus the minimum value). This transform maps the minimum value to 0 and the maximum value to 1, resulting in a list of numbers in the unit range [0, 1].