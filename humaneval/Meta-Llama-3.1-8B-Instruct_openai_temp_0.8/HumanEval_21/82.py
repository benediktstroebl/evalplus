### Rescale to Unit Interval
#### Python Script

```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of float numbers

    Returns:
        List[float]: The list of numbers scaled to the unit interval [0, 1]
    """
    # Ensure the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = np.min(numbers)
    max_value = np.max(numbers)

    # Check if all numbers are identical
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transform to the list
    scaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return scaled_numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers as input and returns the list scaled to the unit interval [0, 1]. The function first checks if the input list has at least two elements. Then, it finds the minimum and maximum values in the list. If all numbers are identical, it returns a list of zeros. Otherwise, it applies a linear transform to the list by subtracting the minimum value from each number and then dividing by the range of the values. The resulting list is returned. The example usage demonstrates how to call the function with a list of numbers and print the scaled list.