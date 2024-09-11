```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Apply a linear transform to the input list of numbers, 
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers (List[float]): A list of numbers (of at least two elements).

    Returns:
        List[float]: The input list with linearly scaled values.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)
    value_range = max_value - min_value

    # Handle the case where all numbers are the same
    if value_range == 0:
        return [1.0] * len(numbers)

    return [(x - min_value) / value_range for x in numbers]


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

In this code:

*   We first check if the input list has at least two elements.
*   We find the minimum and maximum values in the list using the built-in `min` and `max` functions.
*   We calculate the range of the values by subtracting the minimum value from the maximum value.
*   We handle the edge case where all numbers in the list are the same, in which case we return a list of ones.
*   Finally, we use a list comprehension to apply the linear transformation to each number in the list. The transformation scales the value to the range [0, 1] by subtracting the minimum value and then dividing by the value range.

This code provides a clear and efficient solution to the problem, with proper error handling and documentation.