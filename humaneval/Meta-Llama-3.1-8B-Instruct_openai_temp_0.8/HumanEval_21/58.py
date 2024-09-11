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

    Raises:
        ValueError: If the input list has less than two elements

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        raise ValueError("All elements in the list must be distinct")

    rescaled = [(x - min_val) / (max_val - min_val) for x in numbers]
    return rescaled

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input, rescales them to the range [0, 1], and returns the resulting list. The function first checks if the input list has at least two elements and all elements are distinct, as required by the problem statement. It then calculates the minimum and maximum values in the list, and uses these values to rescale the list. The rescaled values are calculated using a list comprehension, which creates a new list with the rescaled values. Finally, the script tests the function with a sample input list and prints the result.