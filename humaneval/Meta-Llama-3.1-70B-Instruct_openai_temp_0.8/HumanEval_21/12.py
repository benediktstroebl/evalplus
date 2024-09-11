```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: A list of numbers (of at least two elements).

    Returns:
        A list of numbers that have been linearly transformed to be between 0 and 1.

    Raises:
        ValueError: If the input list has less than two elements.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    # Handle the case where all numbers are the same
    if max_num == min_num:
        return [0.0] * len(numbers)

    range_num = max_num - min_num

    return [(num - min_num) / range_num for num in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([10.0, 20.0, 30.0, 40.0, 50.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
print(rescale_to_unit([5.0, 5.0, 5.0, 5.0, 5.0]))  # [0.0, 0.0, 0.0, 0.0, 0.0]
```