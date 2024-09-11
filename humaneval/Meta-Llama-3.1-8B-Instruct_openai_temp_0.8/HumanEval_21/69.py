```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A rescaled list of floating point numbers
    """
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        return [0.0] * len(numbers)

    rescaled = [(num - min_value) / (max_value - min_value) for num in numbers]
    return rescaled

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function which accepts a list of floating point numbers and returns a new list where the values have been rescaled to the range [0, 1]. The script includes an error check to ensure that the input list has at least two elements. It also handles the edge case where the minimum and maximum values are the same. The script includes an example usage of the function to demonstrate its output.