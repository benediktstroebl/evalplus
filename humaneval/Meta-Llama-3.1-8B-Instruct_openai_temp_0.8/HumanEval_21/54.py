```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers: A list of float numbers

    Returns:
        A list of float numbers scaled to the unit interval [0, 1]

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if all numbers are equal
    if min_num == max_num:
        return [0.0] * len(numbers)

    # Apply the linear transform to the list
    rescaled_numbers = [(n - min_num) / (max_num - min_num) for n in numbers]

    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```