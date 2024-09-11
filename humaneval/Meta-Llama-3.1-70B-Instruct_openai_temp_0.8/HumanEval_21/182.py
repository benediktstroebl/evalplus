```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of floating point numbers with at least two elements.

    Returns:
    List[float]: The rescaled list of numbers.
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check for the case where all numbers are the same
    if max_num == min_num:
        return [1.0] * len(numbers)

    # Calculate the scaling factor
    scale_factor = 1 / (max_num - min_num)

    # Apply the linear transformation to the list of numbers
    rescaled_numbers = [(num - min_num) * scale_factor for num in numbers]

    return rescaled_numbers


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```