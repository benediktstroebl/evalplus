```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of numbers

    Returns:
    List[float]: The rescaled list of numbers

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

    # Check if the minimum and maximum numbers are the same
    if min_num == max_num:
        # If they are the same, return a list of zeros
        return [0.0] * len(numbers)

    # Apply the linear transform
    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where the numbers have been linearly transformed to the range [0, 1]. The transformation is done by subtracting the minimum number from each number and then dividing by the range of the numbers (i.e., the difference between the maximum and minimum numbers). If the list has less than two elements, the function raises a ValueError. If the minimum and maximum numbers are the same, the function returns a list of zeros. The script includes an example usage of the function.