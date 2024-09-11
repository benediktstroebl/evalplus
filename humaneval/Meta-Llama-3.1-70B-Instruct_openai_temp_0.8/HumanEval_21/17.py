```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers: A list of floats with at least two elements.

    Returns:
    A list of floats where the smallest number in the input list is 0 and the largest is 1.
    """

    # Check if the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Calculate the range of the numbers
    num_range = max_num - min_num

    # If all numbers are the same, return a list of zeros
    if num_range == 0:
        return [0.0] * len(numbers)

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(num - min_num) / num_range for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```