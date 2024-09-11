```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers: A list of float numbers

    Returns:
        A list of float numbers rescaled to the unit range [0, 1]
    
    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")
    
    # Find the minimum and maximum numbers in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check if all numbers in the list are equal
    if min_value == max_value:
        raise ValueError("The list must have distinct numbers")
    
    # Apply the linear transform
    rescaled_numbers = [(n - min_value) / (max_value - min_value) for n in numbers]
    
    return rescaled_numbers

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This Python script defines a function `rescale_to_unit` that takes a list of float numbers as input and returns a new list with the same numbers rescaled to the unit range [0, 1]. The function first checks if the input list has at least two elements and if all numbers in the list are distinct. It then finds the minimum and maximum numbers in the list and applies a linear transform to rescale the numbers. The script includes a test case to demonstrate the function's behavior.