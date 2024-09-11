```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers: A list of at least two float numbers

    Returns:
    A list of float numbers after applying linear transform

    Raises:
    ValueError: If the input list has less than two elements
    """

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Calculate the range of the numbers
    num_range = max_num - min_num

    # If the range is zero, all numbers are the same, so return a list of zeros
    if num_range == 0:
        return [0.0] * len(numbers)

    # Apply linear transformation to the numbers
    rescaled_numbers = [(num - min_num) / num_range for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```