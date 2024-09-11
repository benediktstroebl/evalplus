### Rescale Numbers to Unit Range
#### Problem Statement
Given a list of numbers, apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
    numbers: A list of at least two float numbers.
    
    Returns:
    A new list where the smallest number is 0 and the largest is 1.
    
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Check for division by zero
    if min_val == max_val:
        raise ValueError("All elements in the list are the same")
    
    # Apply linear transformation
    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers rescaled to the unit range [0, 1]. It first checks if the list has at least two elements and if all elements are the same (in which case the transformation would be invalid). If these conditions are met, it applies the linear transformation by subtracting the minimum value and dividing by the range of the input numbers. Finally, an example usage is provided to demonstrate the function's behavior.