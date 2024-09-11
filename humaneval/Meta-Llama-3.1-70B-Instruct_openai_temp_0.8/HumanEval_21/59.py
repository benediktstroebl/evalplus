```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of numbers with at least two elements.
    
    Returns:
        List[float]: The rescaled list of numbers.
    """
    
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")
    
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Check for the case where all numbers are equal
    if max_value == min_value:
        return [1.0 for _ in numbers]
    
    # Apply the linear transformation
    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]
    
    return rescaled_numbers


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```