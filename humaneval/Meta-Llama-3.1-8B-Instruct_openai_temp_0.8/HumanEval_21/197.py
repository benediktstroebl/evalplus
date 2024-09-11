```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of floating point numbers.
        
    Returns:
        List[float]: The list of numbers scaled to the unit interval [0, 1].
        
    Raises:
        ValueError: If the list has less than two elements.
        
    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check for division by zero
    if max_value == min_value:
        # In this case, all numbers are the same, so return a list of zeros
        return [0.0] * len(numbers)
    
    # Apply the linear transformation
    return [(x - min_value) / (max_value - min_value) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines the `rescale_to_unit` function, which rescales a list of numbers to the unit interval [0, 1]. It first checks if the list has at least two elements, and raises a `ValueError` if it doesn't. If the list has two or more elements, it finds the minimum and maximum values in the list, and then applies a linear transformation to each number in the list, subtracting the minimum value and dividing by the range of the values. If the minimum and maximum values are the same, all numbers are the same, so the function returns a list of zeros. The script then demonstrates the function's usage with an example list of numbers.