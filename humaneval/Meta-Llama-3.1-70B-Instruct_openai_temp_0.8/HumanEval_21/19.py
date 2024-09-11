```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
    numbers (List[float]): A list of floating point numbers.
    
    Returns:
    List[float]: The rescaled list of numbers.
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")
    
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Check if the minimum and maximum values are equal
    if min_val == max_val:
        raise ValueError("The input list must have at least two distinct elements")
    
    # Calculate the scaling factor
    scaling_factor = 1 / (max_val - min_val)
    
    # Apply the linear transformation to the list
    rescaled_numbers = [(num - min_val) * scaling_factor for num in numbers]
    
    return rescaled_numbers


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```