```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Use numpy to find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)

    # Apply the linear transform
    rescaled_numbers = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script uses the NumPy library to find the minimum and maximum values in the list, and then applies a linear transform to the list. The `rescale_to_unit` function takes a list of numbers as input, and returns a new list where the smallest number is 0 and the largest number is 1. If the input list has less than two elements, the function raises a `ValueError`.