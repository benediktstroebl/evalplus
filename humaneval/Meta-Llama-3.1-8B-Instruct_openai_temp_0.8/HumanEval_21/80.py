```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of at least two numbers.
    
    Returns:
        List[float]: The rescaled list of numbers.
    
    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    
    # Ensure the list is not empty and contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")
    
    # Find the minimum and maximum values in the list
    min_value = np.min(numbers)
    max_value = np.max(numbers)
    
    # Check for division by zero
    if min_value == max_value:
        raise ZeroDivisionError("All values in the list must be different.")
    
    # Apply the linear transform
    scaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]
    
    return scaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```