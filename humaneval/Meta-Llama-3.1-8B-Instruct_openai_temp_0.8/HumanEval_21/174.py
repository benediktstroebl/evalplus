### Linear Rescaling of Numbers to Unit Range
#### Problem Description
Transform a list of numbers to a unit range, where the smallest number becomes 0 and the largest becomes 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers: List of floating point numbers
    
    Returns:
        List of floating point numbers in the unit range (0 to 1)
    
    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All numbers in the list are the same")
    
    # Apply the linear transform
    rescaled = [(x - min_val) / (max_val - min_val) for x in numbers]
    
    return rescaled

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```