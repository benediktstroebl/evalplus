```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of floating point numbers, rescaled to the unit interval [0, 1]

    Raises:
        ValueError: If the input list has less than two elements
    """
    
    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value == min_value:
        raise ValueError("All values in the input list must be different")

    # Apply the linear transform to the list
    rescaled_numbers = [(x - min_value) / (max_value - min_value) for x in numbers]

    return rescaled_numbers


# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of floating point numbers as input and returns a new list with the same numbers, but rescaled to the unit interval [0, 1]. The rescaling is done by applying a linear transform to each number in the list, such that the smallest number becomes 0 and the largest number becomes 1.

The function first checks if the input list has at least two elements, and raises a `ValueError` if not. It then finds the minimum and maximum values in the list, and applies the linear transform to each number in the list. The transformed numbers are stored in a new list, which is returned by the function.

The script also includes a test of the function with the example input `[1.0, 2.0, 3.0, 4.0, 5.0]`, and prints the output of the function, which is `[0.0, 0.25, 0.5, 0.75, 1.0]`.