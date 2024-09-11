```markdown
### Rescaling a List of Numbers to the Unit Interval

This script defines a function `rescale_to_unit` that takes a list of numbers and applies a linear transformation to rescale them to the unit interval [0, 1].

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): The list of numbers to be rescaled

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")
    
    min_val = min(numbers)
    max_val = max(numbers)
    
    if max_val == min_val:
        return [0.0] * len(numbers)
    
    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script first checks if the input list has at least two elements. If not, it raises a `ValueError`. Then it finds the minimum and maximum values in the list. If all numbers are equal, it returns a list of zeros. Otherwise, it applies the linear transformation to each number in the list by subtracting the minimum value and dividing by the range of the list. The result is a list of numbers in the unit interval [0, 1].