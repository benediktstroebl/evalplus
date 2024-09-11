```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers with at least two elements

    Returns:
        List[float]: The rescaled list of numbers
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for edge case where all numbers are the same
    if min_val == max_val:
        return [1.0] * len(numbers)

    # Apply the linear transformation to each number in the list
    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest number is 1. The function first checks if the input list has at least two elements. Then, it finds the minimum and maximum values in the list. If all numbers are the same, it returns a list of 1s. Otherwise, it applies a linear transformation to each number in the list using a list comprehension. The example usage at the end demonstrates how to use the function.