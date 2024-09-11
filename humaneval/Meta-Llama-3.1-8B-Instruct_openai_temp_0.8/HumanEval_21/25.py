### Rescaling a List of Numbers to Unit Interval
```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Rescale a list of numbers to the unit interval [0, 1].

    Given a list of numbers, apply a linear transform to that list, 
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of at least two elements.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Ensure the list has at least two elements
    assert len(numbers) > 1, "List must have at least two elements"

    # Find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # Apply the linear transform
    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script uses the `numpy` library to efficiently find the minimum and maximum values in the list. The linear transform is then applied using a list comprehension.