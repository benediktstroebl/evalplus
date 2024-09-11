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
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for the special case where all numbers are the same
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    rescaled_numbers = rescale_to_unit(numbers)
    print(f"Rescaled numbers: {rescaled_numbers}")
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest number is 1. The function uses a linear transformation to achieve this, where each number `x` in the input list is mapped to `(x - min_value) / (max_value - min_value)`, where `min_value` and `max_value` are the smallest and largest numbers in the input list, respectively. If the input list has less than two elements, the function raises a `ValueError`. The example usage at the end of the script demonstrates how to use the `rescale_to_unit` function.