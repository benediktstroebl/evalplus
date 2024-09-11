```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers: A list of at least two float numbers.

    Returns:
    A list of float numbers, where the smallest number in the input list is 0 
    and the largest number is 1.
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # If all numbers are the same, return a list with the same number of 1s
    if min_value == max_value:
        return [1.0] * len(numbers)

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]
    
    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```