```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of numbers with at least two elements.

    Returns:
    List[float]: The rescaled list of numbers.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_value == max_value:
        # If they are the same, return a list of zeros with the same length as the input list
        return [0.0] * len(numbers)

    # Calculate the range of the values
    range_value = max_value - min_value

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(num - min_value) / range_value for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled = rescale_to_unit(numbers)
print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```