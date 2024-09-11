Here's the Python script that solves the problem:
```markdown
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A list of numbers rescaled to the range [0, 1].

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Apply a linear transform to rescale the numbers to the range [0, 1]
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```
This script uses a list comprehension to apply a linear transform to each number in the input list. The transform is calculated as `(x - min_value) / (max_value - min_value)`, where `x` is the current number, `min_value` is the smallest number in the list, and `max_value` is the largest number in the list. The result is a new list of numbers in the range [0, 1].