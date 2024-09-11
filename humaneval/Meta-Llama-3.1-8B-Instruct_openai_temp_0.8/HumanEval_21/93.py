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
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.0] * len(numbers)

    return [(x - min_val) / (max_val - min_val) for x in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This Python script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers rescaled to the interval [0, 1]. The rescaling is done using a linear transformation, where the smallest number in the input list becomes 0 and the largest becomes 1. If the input list has less than two elements, the function raises a `ValueError`. The script also includes a test case to demonstrate the function's behavior.