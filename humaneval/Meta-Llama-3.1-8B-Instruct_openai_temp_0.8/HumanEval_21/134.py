### Rescaling List of Numbers to Unit Range

```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two float numbers.

    Returns:
        List[float]: A rescaled list of numbers in the unit range [0, 1].

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Ensure the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # Check if all numbers are equal
    if max_val - min_val == 0:
        return [numbers[0] for _ in range(len(numbers))]

    # Apply linear transform to rescale the list to unit range
    rescaled_list = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled_list

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the numbers are rescaled to the unit range [0, 1]. It first checks if the input list has at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum values in the list. If all numbers are equal, it returns a list where all numbers are equal to the first number in the input list. Otherwise, it applies a linear transform to rescale the list to the unit range. The test at the end of the script demonstrates how to use the function.