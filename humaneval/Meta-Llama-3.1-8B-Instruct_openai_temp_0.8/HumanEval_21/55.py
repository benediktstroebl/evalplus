```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): Input list of numbers

    Returns:
        List[float]: Rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        return [0.0] * len(numbers)

    rescaled = [(num - min_num) / (max_num - min_num) for num in numbers]
    return rescaled


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the numbers are rescaled to the range [0, 1]. The `min` and `max` functions are used to find the smallest and largest numbers in the input list. If the input list has only one unique value, the function returns a list of zeros.

The script includes a docstring to explain how the function works, and provides an example usage at the end to demonstrate how to call the function.