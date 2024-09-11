```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): The input list of numbers.

    Returns:
    List[float]: The rescaled list of numbers.
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Calculate the range of the values
    value_range = max_value - min_value

    # Rescale the values using a linear transformation
    rescaled_numbers = [(value - min_value) / value_range for value in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```