```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Args:
        numbers (List[float]): A list of floating point numbers
    Returns:
        List[float]: The list of numbers rescaled to the unit interval [0, 1]
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")
    
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check if all numbers are the same
    if min_value == max_value:
        return [0.0] * len(numbers)
    
    # Apply the linear transform
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]
    
    return rescaled_numbers

# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input, scales them to the unit interval [0, 1], and returns the rescaled list. The function first checks if the input list has at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum values in the list, and applies a linear transform to each element in the list, mapping the minimum value to 0 and the maximum value to 1. If all numbers in the list are the same, it returns a list of zeros. The example usage at the end demonstrates how to use the function.