```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, rescaling them to the range [0, 1].
    
    The smallest number in the list will become 0 and the largest will become 1.
    
    Args:
        numbers: A list of at least two float numbers.
    
    Returns:
        A new list with the same length as the input, containing the rescaled numbers.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Handle the case where all numbers are the same
    if min_value == max_value:
        return [0.0] * len(numbers)
    
    # Calculate the scaling factor and offset
    scaling_factor = 1 / (max_value - min_value)
    offset = -min_value * scaling_factor
    
    # Apply the linear transformation to each number in the list
    return [(n * scaling_factor) + offset for n in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```