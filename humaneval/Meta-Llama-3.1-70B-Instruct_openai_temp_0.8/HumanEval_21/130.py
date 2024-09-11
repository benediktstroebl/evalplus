```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to the input list of numbers, 
    such that the smallest number becomes 0 and the largest becomes 1.

    Args:
        numbers: A list of at least two float numbers.

    Returns:
        A list of float numbers with the same length as the input, 
        rescaled to the unit interval [0, 1].

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_num = min(numbers)
    max_num = max(numbers)

    # Avoid division by zero
    if max_num == min_num:
        return [0.0] * len(numbers)

    range_num = max_num - min_num
    return [(num - min_num) / range_num for num in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```