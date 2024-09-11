### Rescale List of Numbers to Unit Interval
#### Problem Description
Given a list of numbers, apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.

#### Solution
```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): List of numbers to rescale

    Returns:
    List[float]: Rescaled list of numbers

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Ensure the list has at least two elements
    assert len(numbers) >= 2, "List must have at least two elements"

    # Find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # Check if all elements in the list are equal
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled_numbers
```

#### Explanation

This solution uses the [NumPy library](https://numpy.org/) to find the minimum and maximum values in the list. It then applies a linear transform to each number in the list, mapping the smallest number to 0 and the largest number to 1. If all elements in the list are equal, it returns a list of zeros. The result is a list of numbers in the unit interval [0, 1].