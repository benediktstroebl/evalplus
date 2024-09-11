### Rescaling Numbers to Unit Interval
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

    Returns:
        List[float]: The rescaled list of numbers
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All elements in the list are equal")

    # Apply the linear transform
    rescaled = [(x - min_val) / (max_val - min_val) for x in numbers]

    return rescaled


# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been rescaled to be between 0 and 1. The rescaling is done using a linear transform, where the smallest number in the original list becomes 0 and the largest number becomes 1. The script also includes example usage and docstrings to explain the function's behavior.