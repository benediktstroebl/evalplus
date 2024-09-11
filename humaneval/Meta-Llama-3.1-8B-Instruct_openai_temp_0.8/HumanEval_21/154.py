```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of at least two float numbers

    Returns:
        List[float]: A list of numbers rescaled to unit range [0, 1]

    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        # Handle the case where all numbers are the same
        return [0.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This Python script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same numbers but rescaled to the unit range [0, 1]. The function first checks if the input list contains at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum values in the list. If all numbers are the same, it returns a list of zeros. Otherwise, it applies a linear transformation to each number by subtracting the minimum value and dividing by the range of the values. The function is tested with an example list.