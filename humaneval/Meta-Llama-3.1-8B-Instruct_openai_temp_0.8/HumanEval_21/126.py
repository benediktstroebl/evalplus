```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of floating point numbers

    Returns:
        List[float]: A list of transformed floating point numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The input list must contain at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    
    if max_num == min_num:
        raise ValueError("All numbers in the list must be different")

    return [(num - min_num) / (max_num - min_num) for num in numbers]

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
transformed_numbers = rescale_to_unit(numbers)
print(transformed_numbers)
```

This Python script defines a function `rescale_to_unit` which takes a list of floating point numbers and returns the list with each number rescaled to be between 0 and 1, inclusive. The script also includes error checking to ensure that the input list contains at least two distinct numbers.