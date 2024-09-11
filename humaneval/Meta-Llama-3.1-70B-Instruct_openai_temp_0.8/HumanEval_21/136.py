```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    Args:
        numbers (List[float]): A list of floating point numbers.
    
    Returns:
        List[float]: The rescaled list of numbers.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_num == max_num:
        # If they are the same, return a list of zeros (since all numbers are the same)
        return [0.0] * len(numbers)
    else:
        # Calculate the range of the values
        range_num = max_num - min_num
        
        # Apply the linear transformation to the list
        rescaled_numbers = [(num - min_num) / range_num for num in numbers]
        
        return rescaled_numbers


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script first checks if the list has at least two elements. It then finds the minimum and maximum values in the list. If the minimum and maximum values are the same, it returns a list of zeros (since all numbers are the same). Otherwise, it calculates the range of the values and applies a linear transformation to the list to rescale the numbers to the range [0, 1]. The rescaled list is then returned.