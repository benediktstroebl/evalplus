```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of floating point numbers

    Returns:
        A list of floating point numbers, where the smallest element is 0 and the largest element is 1

    Raises:
        ValueError: If the input list has less than 2 elements
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least 2 elements")

    min_value = min(numbers)
    max_value = max(numbers)
    
    if min_value == max_value:
        # If all numbers are the same, return a list of 1.0
        return [1.0] * len(numbers)
    
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number becomes 0 and the largest number becomes 1. The function uses a linear transformation to achieve this, by subtracting the minimum value and then dividing by the range of the input numbers. The example usage at the end demonstrates how to use this function.