```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): The list of numbers to rescale

    Returns:
        List[float]: The rescaled list

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(num - min_val) / (max_val - min_val) for num in numbers]

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```