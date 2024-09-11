```python
from typing import List
import numpy as np

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): List of numbers to be rescaled

    Returns:
        List[float]: Rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    # Find the minimum and maximum values in the list
    min_val = np.min(numbers)
    max_val = np.max(numbers)
    
    # Check if all numbers are equal
    if min_val == max_val:
        return [0.0] * len(numbers)
    
    # Apply linear transform
    rescaled = [(num - min_val) / (max_val - min_val) for num in numbers]
    
    return rescaled

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script uses NumPy for efficient computation of the minimum and maximum values. It also includes a check to handle the case where all numbers in the list are equal. In this case, the function returns a list of zeros.