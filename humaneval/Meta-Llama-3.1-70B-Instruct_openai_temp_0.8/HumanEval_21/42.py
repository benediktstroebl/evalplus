```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers: A list of numbers (of at least two elements)

    Returns:
    A list of numbers where the smallest number is 0 and the largest is 1
    """
    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same to avoid division by zero
    if max_value == min_value:
        return [1.0] * len(numbers)

    # Apply the linear transformation
    return [(x - min_value) / (max_value - min_value) for x in numbers]


# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function as specified, and includes a docstring to describe what the function does and how to use it. The example usage at the end demonstrates how to use the function with the provided test case.