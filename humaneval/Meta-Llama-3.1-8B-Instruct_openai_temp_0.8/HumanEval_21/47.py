```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the input list has less than two elements.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the smallest and largest numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if all numbers are identical
    if min_num == max_num:
        raise ValueError("All numbers in the list are identical")

    # Apply the linear transform
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers and returns a new list with the same numbers but rescaled to the interval [0, 1]. The rescaling is done by applying a linear transform, where the smallest number in the original list becomes 0 and the largest number becomes 1. The script also includes example usage and documentation.