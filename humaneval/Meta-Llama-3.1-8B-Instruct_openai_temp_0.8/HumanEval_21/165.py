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

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are equal (which would prevent division by zero)
    if min_value == max_value:
        raise ValueError("All numbers are equal, cannot rescale")

    # Calculate the rescaled values
    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return rescaled_numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines the `rescale_to_unit` function as specified, and includes example usage and input validation. The function calculates the minimum and maximum values in the input list, checks for potential division by zero, and then applies the linear transform to each number in the list. The result is a new list of rescaled numbers.