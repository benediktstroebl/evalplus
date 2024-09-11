```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of float numbers

    Returns:
        A list of float numbers where the smallest number is 0 and the largest is 1

    Raises:
        ValueError: If the input list has less than two elements

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val - min_val == 0:
        # All numbers are equal, return a list of zeros
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

In this code, we first check if the input list has at least two elements. If not, we raise a ValueError. Then, we calculate the minimum and maximum values in the list. If all numbers are equal, we return a list of zeros. Otherwise, we apply the linear transformation to each number in the list by subtracting the minimum value and dividing by the range of the values.