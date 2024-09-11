### Rescaling a List of Numbers to Unit Interval
#### Problem Description
Given a list of numbers, perform a linear transformation to scale the smallest number to 0 and the largest to 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): The input list of numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        # If all numbers are equal, return a list of zeros
        return [0.0] * len(numbers)

    # Apply the linear transformation
    rescaled = [(n - min_val) / (max_val - min_val) for n in numbers]

    return rescaled
```

#### Usage
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```