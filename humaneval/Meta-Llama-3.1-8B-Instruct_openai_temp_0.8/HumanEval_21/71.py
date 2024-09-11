### Rescaling a List of Numbers to Unit Interval

The following Python script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers rescaled to the unit interval [0, 1].

```markdown
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
    """
    # Ensure input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All numbers in the list are the same")

    # Apply linear transformation to rescale the list
    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script uses a list comprehension to apply the linear transformation to each number in the input list. The transformation is defined as `(n - min_val) / (max_val - min_val)`, where `n` is the current number, `min_val` is the minimum value in the list, and `max_val` is the maximum value in the list. The resulting list of rescaled numbers is then returned.