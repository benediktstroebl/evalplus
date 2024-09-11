```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled.

    Returns:
        List[float]: Rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List should have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        return [0.0] * len(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

This script first checks if the input list has at least two elements. If not, it raises a ValueError. Then it finds the minimum and maximum numbers in the list. If the maximum and minimum are the same, it returns a list of zeros. Otherwise, it applies a linear transformation to each number in the list by subtracting the minimum and dividing by the range (maximum - minimum) of the list. The result is a list of numbers between 0 and 1.