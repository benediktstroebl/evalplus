```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), 
    apply a linear transform to that list, 
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
    numbers (List[float]): A list of floating point numbers
    
    Returns:
    List[float]: A list of floating point numbers rescaled to the unit interval
    """
    
    # Check if list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check if all numbers are the same
    if min_value == max_value:
        raise ValueError("All numbers in the list are the same")
    
    # Apply the linear transform
    rescaled_numbers = [(n - min_value) / (max_value - min_value) for n in numbers]
    
    return rescaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list with the same numbers, but rescaled to the unit interval [0, 1]. It first checks if the list has at least two elements and if all numbers are different. If not, it raises a `ValueError`. Otherwise, it applies the linear transformation to each number in the list, and returns the resulting list. The test at the end shows how to use this function.