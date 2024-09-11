```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of numbers with at least two elements.

    Returns:
    List[float]: The rescaled list of numbers.

    Raises:
    ValueError: If the input list has less than two elements.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Calculate the range of the values
    range_value = max_value - min_value

    # If all numbers are the same, return a list of 0s
    if range_value == 0:
        return [0.0] * len(numbers)

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(num - min_value) / range_value for num in numbers]

    return rescaled_numbers


# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This Python script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number is rescaled to 0 and the largest number is rescaled to 1. The function uses list comprehension to apply the linear transformation to each number in the input list. The transformation is calculated based on the minimum and maximum values in the list. The script also includes error checking to ensure that the input list has at least two elements.