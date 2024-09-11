### Rescaling Numbers to Unit Interval
#### Problem Description
Given a list of numbers, apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transform to a list of numbers, such that the smallest number becomes 0 and the largest becomes 1.
    
    Args:
    numbers (List[float]): A list of at least two elements.
    
    Returns:
    List[float]: The transformed list with values in the unit interval [0, 1].
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")
    
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check if the minimum and maximum values are the same
    if min_value == max_value:
        raise ValueError("All elements in the list must be different.")
    
    # Apply the linear transform
    transformed = [(n - min_value) / (max_value - min_value) for n in numbers]
    
    return transformed

### Example Usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers rescaled to the unit interval [0, 1]. The function first checks if the input list has at least two elements and if all elements are different. If not, it raises a `ValueError`. Otherwise, it applies a linear transform to the list by subtracting the minimum value and dividing by the range of the input values. The transformed list is then returned.