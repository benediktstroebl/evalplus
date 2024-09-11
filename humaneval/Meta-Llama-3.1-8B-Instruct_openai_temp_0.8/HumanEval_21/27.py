```python
from typing import List
import numpy as np


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two float numbers

    Returns:
        List[float]: The list of numbers transformed to be between 0 and 1

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers")

    # Convert the list to a numpy array for easier manipulation
    numbers_array = np.array(numbers)

    # Find the minimum and maximum values in the array
    min_value = np.min(numbers_array)
    max_value = np.max(numbers_array)

    # Apply the linear transform
    rescaled_array = (numbers_array - min_value) / (max_value - min_value)

    # Convert the numpy array back to a list
    rescaled_list = rescaled_array.tolist()

    return rescaled_list


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script uses the NumPy library to make the linear transformation more efficient. It first checks if the input list has at least two elements, then finds the minimum and maximum values in the list. The linear transformation is applied by subtracting the minimum value from each number and then dividing by the range of the numbers. The result is converted back to a list and returned.