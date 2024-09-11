```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")
    
    # Use NumPy to find the minimum and maximum values in the list
    min_value = np.min(numbers)
    max_value = np.max(numbers)
    
    # Calculate the range of the list
    range_value = max_value - min_value
    
    # Check if the range is zero to avoid division by zero
    if range_value == 0:
        return [0.0] * len(numbers)
    
    # Apply the linear transform to each element in the list
    rescaled_numbers = [(num - min_value) / range_value for num in numbers]
    
    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```