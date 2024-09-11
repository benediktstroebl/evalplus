```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The list of numbers rescaled to the unit interval.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    if max_val - min_val == 0:
        raise ValueError("All elements in the list must be distinct")
    
    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

In this script, the function `rescale_to_unit` takes a list of numbers as input, finds the minimum and maximum values in the list, and then applies a linear transformation to each number in the list. The transformation maps the minimum value to 0 and the maximum value to 1. The function also includes input validation to ensure that the list contains at least two distinct elements.