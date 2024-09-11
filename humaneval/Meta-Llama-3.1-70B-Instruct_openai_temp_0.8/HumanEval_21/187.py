```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the given list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A list of float numbers where the smallest input number is 0 and the largest is 1.

    Raises:
        ValueError: If the input list has less than two elements.
    """

    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)

    if max_value == min_value:
        # Handle the case where all numbers are the same
        return [1.0] * len(numbers)

    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]

# Edge case: all numbers are the same
print(rescale_to_unit([1.0, 1.0, 1.0, 1.0]))  # Output: [1.0, 1.0, 1.0, 1.0]

# Invalid input
try:
    print(rescale_to_unit([1.0]))
except ValueError as e:
    print(e)  # Output: Input list must have at least two elements.
```