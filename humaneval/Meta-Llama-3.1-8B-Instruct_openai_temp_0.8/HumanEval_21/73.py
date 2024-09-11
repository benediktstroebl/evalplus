```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of floating point numbers
    
    Returns:
        List[float]: The rescaled list of numbers
    
    Raises:
        ValueError: If the input list has less than two elements
    
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check if the minimum and maximum values are the same
    if min_value == max_value:
        # If the minimum and maximum values are the same, return a list of zeros
        return [0.0] * len(numbers)
    
    # Apply the linear transform to the list
    rescaled_list = [(num - min_value) / (max_value - min_value) for num in numbers]
    
    return rescaled_list

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list with the same elements rescaled to the range [0, 1]. The function first checks if the input list has at least two elements, and raises a `ValueError` if it does not. It then finds the minimum and maximum values in the list, and applies a linear transform to the list using these values. If the minimum and maximum values are the same, the function returns a list of zeros. The script also includes an example usage of the function.