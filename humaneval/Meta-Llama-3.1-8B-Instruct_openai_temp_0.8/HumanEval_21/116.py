```python
from typing import List
import math

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

    Returns:
        List[float]: The rescaled list of numbers

    Raises:
        ValueError: If the list contains less than two elements
    """

    # Check if the list contains less than two elements
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if all numbers are the same
    if min_num == max_num:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(n - min_num) / (max_num - min_num) for n in numbers]

    return rescaled_numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns the rescaled list. The function first checks if the list contains less than two elements and raises a `ValueError` if so. It then finds the minimum and maximum numbers in the list. If all numbers are the same, it returns a list of zeros. Otherwise, it applies a linear transform to each number in the list, subtracting the minimum number and dividing by the range of the numbers, and returns the resulting list. The example usage shows how to use this function with a list of numbers.