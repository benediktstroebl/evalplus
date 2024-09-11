```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of numbers
    Returns:
    List[float]: The list of numbers rescaled to unit
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    if min_num == max_num:
        return [0.0] * len(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the numbers have been scaled to the range [0, 1]. The script then tests the function with the example provided and prints the result. 

If the input list contains less than two elements, the function raises a `ValueError` to prevent it from operating on an empty or singleton list. 

Additionally, if the input list contains numbers that are all equal (i.e., the minimum and maximum are the same), the function returns a list of zeros.