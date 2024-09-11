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
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if min_num == max_num:
        return [0.0] * len(numbers)

    scaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]
    return scaled_numbers


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input and returns a new list with the same numbers, but rescaled so that the smallest number is 0 and the largest number is 1. The function first checks if the input list has at least two elements. If not, it raises a `ValueError`. It then finds the minimum and maximum numbers in the list. If the minimum and maximum numbers are the same, it returns a list of zeros. Otherwise, it uses a list comprehension to calculate the rescaled numbers and returns the result.

The script also includes an example usage of the `rescale_to_unit` function, which demonstrates how to call the function with a sample list of numbers and print the rescaled result.