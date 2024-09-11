### Rescaling Numbers to Unit Interval
```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): Input list of numbers

    Returns:
        List[float]: Rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_value = np.min(numbers)
    max_value = np.max(numbers)

    if max_value == min_value:
        return [0.0] * len(numbers)

    rescaled_numbers = [(n - min_value) / (max_value - min_value) for n in numbers]
    return rescaled_numbers
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers, but rescaled to the unit interval [0, 1]. The script uses NumPy to find the minimum and maximum values in the input list, and then applies a linear transformation to each number in the list to rescale it to the unit interval. If the input list contains only one element, or if all elements are the same, the function raises a `ValueError`, since in these cases it would not be possible to rescale the numbers to the unit interval.