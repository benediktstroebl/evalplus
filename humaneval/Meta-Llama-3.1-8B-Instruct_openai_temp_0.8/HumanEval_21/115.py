### Rescaling a List of Numbers to the Unit Interval

The following Python script defines a function `rescale_to_unit` that takes a list of numbers and applies a linear transformation to rescale the numbers to the unit interval [0, 1].

```markdown
### Code
```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of float numbers.

    Returns:
        A list of float numbers in the unit interval [0, 1].

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # Apply the linear transformation
    unit_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]

    return unit_numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

### Explanation

The `rescale_to_unit` function takes a list of float numbers as input and returns a new list with the same numbers rescaled to the unit interval [0, 1].

1.  First, it checks if the input list has at least two elements. If not, it raises a `ValueError`.
2.  Then, it finds the minimum and maximum values in the list using `np.min` and `np.max` from the NumPy library.
3.  Finally, it applies the linear transformation to each number in the list by subtracting the minimum value and dividing by the difference between the maximum and minimum values. This ensures that the smallest number becomes 0 and the largest becomes 1.

Note that this function uses a list comprehension to efficiently create the output list. It also uses NumPy functions to find the minimum and maximum values in the list, which is more efficient than using Python's built-in `min` and `max` functions.