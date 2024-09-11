### Rescaling a List of Numbers to Unit Range
#### Self-Contained Python Script

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
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All numbers are equal, cannot rescale")

    # Apply the linear transform
    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```