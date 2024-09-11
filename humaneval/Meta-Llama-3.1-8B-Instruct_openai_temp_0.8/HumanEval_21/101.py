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

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)

    if max_num == min_num:
        return [0.0] * len(numbers)

    return [(n - min_num) / (max_num - min_num) for n in numbers]

# Testing the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where the smallest number is 0 and the largest number is 1. It first checks if the input list has at least two elements, because the rescaling operation is not possible with a single element. If the list has two elements, and those two elements are equal, it returns a list where all elements are 0. Otherwise, it uses a list comprehension to apply the linear transformation to each element in the list. The function also includes a docstring with information about its input, output, and an example use case.