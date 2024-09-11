### Rescale Numbers to Unit Range
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): List of numbers to rescale.

    Returns:
        List[float]: Rescaled list of numbers.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        raise ValueError("List must have distinct elements")

    return [(n - min_num) / (max_num - min_num) for n in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been rescaled to the unit range [0, 1]. The function first checks if the input list has at least two elements and contains distinct elements. If not, it raises a `ValueError`. Otherwise, it calculates the minimum and maximum values in the list, and then uses a list comprehension to rescale each number to the unit range. The result is printed to the console in the example usage section.