```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers
    """
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if max_value == min_value:
        raise ValueError("All numbers are equal, cannot rescale")

    range_value = max_value - min_value
    return [(n - min_value) / range_value for n in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```