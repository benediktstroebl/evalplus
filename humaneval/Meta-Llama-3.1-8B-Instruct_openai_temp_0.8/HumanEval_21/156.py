```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): List of numbers to be rescaled
    
    Returns:
        List[float]: Rescaled list of numbers
    
    Raises:
        ValueError: If the list contains less than two elements
    """
    
    # Check if the list contains less than two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check if the minimum and maximum values are the same
    if min_value == max_value:
        raise ValueError("All values in the list are the same")
    
    # Apply the linear transform to the list
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]
    
    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that rescales the input list of numbers to the unit interval [0, 1]. The function first checks if the input list contains at least two elements. If not, it raises a ValueError. Then it finds the minimum and maximum values in the list and applies a linear transform to the list to map the minimum value to 0 and the maximum value to 1. The function returns the rescaled list of numbers. The script includes a test case to demonstrate the function's behavior.