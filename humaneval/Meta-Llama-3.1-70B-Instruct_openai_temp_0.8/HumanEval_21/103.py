```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of numbers (of at least two elements)

    Returns:
    List[float]: The rescaled list of numbers
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        # If all numbers are the same, return a list with the same value
        return [0.0] * len(numbers)

    # Apply the linear transformation
    rescaled_numbers = [(num - min_num) / (max_num - min_num) for num in numbers]

    return rescaled_numbers


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```