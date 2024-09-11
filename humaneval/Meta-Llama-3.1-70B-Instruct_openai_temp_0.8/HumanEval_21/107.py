```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
    numbers (List[float]): A list of floating point numbers.

    Returns:
    List[float]: The rescaled list of numbers.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        return [1.0] * len(numbers)  # Handle the case where all numbers are equal

    # Calculate the range of the input list
    range_value = max_value - min_value

    # Apply the linear transformation
    rescaled_numbers = [(n - min_value) / range_value for n in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```