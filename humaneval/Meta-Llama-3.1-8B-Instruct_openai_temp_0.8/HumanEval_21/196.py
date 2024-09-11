```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of floating point numbers in the range [0, 1]

    Raises:
        ValueError: If the input list has less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        # Handle the case where all numbers are equal
        return [0.0] * len(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)
```

This script defines the `rescale_to_unit` function, which scales a list of numbers to the range [0, 1] by applying a linear transformation. It first checks if the input list has at least two elements, and raises a ValueError if not. Then it finds the minimum and maximum values in the list, and applies the transformation to each number. If all numbers in the list are equal, it returns a list of zeros. Finally, it demonstrates the usage of the function with an example list of numbers.