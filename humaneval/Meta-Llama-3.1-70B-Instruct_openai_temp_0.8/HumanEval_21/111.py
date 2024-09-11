```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers: A list of at least two floating point numbers

    Returns:
    A new list where the smallest number from the input list is 0 and the largest is 1
    """
    # Check that the input list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check that the minimum and maximum values are not the same
    if min_val == max_val:
        raise ValueError("Input list must contain at least two distinct elements")

    # Apply the linear transformation
    return [(x - min_val) / (max_val - min_val) for x in numbers]


# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines the `rescale_to_unit` function as specified, along with error checking to ensure the input list has at least two distinct elements. It then uses a list comprehension to apply the linear transformation, subtracting the minimum value from each number and then dividing by the range of values. The transformed list is then returned.