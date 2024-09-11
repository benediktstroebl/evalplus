### Linear Rescaling to Unit Range

Here's a Python function that rescales a list of numbers to the unit range [0, 1]:

```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    List[float]: A list of floating point numbers rescaled to the unit range [0, 1].

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # If all values are the same, return a list with all values equal to 0
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This function uses a list comprehension to apply the linear transform to each number in the input list. It first checks if the list has at least two elements and raises a ValueError if not. It then finds the minimum and maximum values in the list using NumPy's `min` and `max` functions. If all values are the same, it returns a list with all values equal to 0. Otherwise, it applies the linear transform by subtracting the minimum value and dividing by the range (max - min).