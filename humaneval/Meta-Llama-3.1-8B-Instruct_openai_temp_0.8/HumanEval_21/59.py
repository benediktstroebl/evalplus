```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

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
        raise ValueError("All numbers in the list are the same, cannot rescale")

    # Apply the linear transform
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script first checks if the list has at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum numbers in the list and applies a linear transform to rescale the numbers. The transform maps the smallest number to 0 and the largest number to 1. If all numbers in the list are the same, it raises a `ValueError` because rescaling is not possible in this case. The rescaled numbers are returned as a list.