```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of float numbers
    
    Returns:
        List[float]: The list of numbers rescaled to unit interval
    
    Raises:
        ValueError: If the list has less than two elements
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")
    
    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)
    
    # Check if the minimum and maximum numbers are the same
    if min_num == max_num:
        # If all numbers are the same, return a list of zeros
        return [0.0] * len(numbers)
    
    # Apply the linear transform to the list
    rescaled = [(n - min_num) / (max_num - min_num) for n in numbers]
    
    return rescaled

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of float numbers as input and returns the list with the smallest number becoming 0 and the largest becoming 1. The function uses a linear transform to achieve this. It also includes error checking to ensure the list has at least two elements. If the minimum and maximum numbers are the same, the function returns a list of zeros. The example usage demonstrates how to use the function with a sample list of numbers.