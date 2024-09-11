```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A list of float numbers, where the smallest number is 0 and the largest is 1.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        # If all numbers are the same, return a list of zeros with the same length
        return [0.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines a function `rescale_to_unit` that applies a linear transformation to a list of numbers. The function first checks if the input list has at least two elements. It then calculates the minimum and maximum values in the list. If all numbers are the same, it returns a list of zeros with the same length. Otherwise, it uses a list comprehension to apply the linear transformation to each number in the list, rescaling it to a value between 0 and 1. The example usage demonstrates how to use the function with a sample list of numbers.