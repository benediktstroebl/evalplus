```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of float numbers

    Returns:
    List[float]: A list of float numbers rescaled to unit interval [0, 1]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This code works by finding the minimum and maximum values in the input list, and then applying a linear transformation to each element in the list. The transformation subtracts the minimum value from each element (shifting the minimum to 0), and then divides by the difference between the maximum and minimum values (scaling the range to 0-1). If the list contains a single value, the function raises a ValueError. If the list contains two or more values, the function returns a list of rescaled values.