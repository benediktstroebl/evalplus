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

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check if the minimum and maximum numbers are the same
    if min_num == max_num:
        raise ValueError("List must contain at least two different numbers")

    # Apply the linear transform to the list
    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
```

This script defines the `rescale_to_unit` function, which takes a list of numbers as input and returns a new list with the same numbers scaled to the range [0, 1]. It first checks if the list contains at least two elements and if the minimum and maximum numbers in the list are different. If these conditions are not met, it raises a `ValueError`. Otherwise, it applies a linear transform to the list to scale the numbers to the range [0, 1] and returns the resulting list. The example usage at the end of the script demonstrates how to use this function with a list of numbers.