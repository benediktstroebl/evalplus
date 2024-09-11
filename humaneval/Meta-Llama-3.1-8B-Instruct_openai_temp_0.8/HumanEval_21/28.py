### Linear Rescaling to Unit Interval
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: The rescaled list of numbers
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if the minimum and maximum values are the same
    if min_val == max_val:
        # If they are the same, return a list of zeros (since there's no range to rescale)
        return [0.0] * len(numbers)

    # Apply the linear transform to the list
    return [(num - min_val) / (max_val - min_val) for num in numbers]

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```
This script defines the `rescale_to_unit` function, which takes a list of floating point numbers and returns a new list with the same numbers, but rescaled to the unit interval [0, 1]. The rescaling is done using a linear transform, where the smallest number in the original list becomes 0 and the largest becomes 1.

The script also includes a check to ensure that the input list has at least two elements, and raises a `ValueError` if it doesn't. If the minimum and maximum values in the list are the same, the function returns a list of zeros, since there's no range to rescale.

Finally, the script includes an example usage of the `rescale_to_unit` function, which prints the rescaled list for the input `[1.0, 2.0, 3.0, 4.0, 5.0]`.