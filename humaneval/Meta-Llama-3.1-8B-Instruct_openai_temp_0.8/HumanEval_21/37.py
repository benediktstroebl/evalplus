```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two floats

    Returns:
        List[float]: The input list with the numbers rescaled to the unit interval

    Raises:
        ValueError: If the input list has less than two elements

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    # Check for division by zero
    if max_num == min_num:
        raise ValueError("Cannot rescale to unit interval: max and min are equal")

    # Use numpy to rescale the numbers
    rescaled_numbers = (numbers - min_num) / (max_num - min_num)

    return rescaled_numbers.tolist()

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function, which takes a list of numbers and returns the same list with the numbers rescaled to the unit interval `[0, 1]`. It uses the `numpy` library to perform the rescaling. If the input list has less than two elements, it raises a `ValueError`. If the maximum and minimum values in the list are equal, it also raises a `ValueError`.