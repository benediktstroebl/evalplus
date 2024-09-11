```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of float numbers
        
    Returns:
        List[float]: A list of float numbers rescaled to the range [0, 1]
    
    Raises:
        ValueError: If the input list contains less than two elements
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    # Find the minimum and maximum numbers in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Check if all numbers in the list are the same
    if min_val == max_val:
        raise ValueError("All numbers in the list are the same")
    
    # Apply the linear transform
    rescaled_numbers = [(num - min_val) / (max_val - min_val) for num in numbers]
    
    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of float numbers and applies a linear transform to rescale the numbers to the range [0, 1]. The function checks if the input list has at least two elements and raises a `ValueError` if the list contains less than two elements or if all numbers in the list are the same. The example usage demonstrates how to use the function to rescale a list of numbers.