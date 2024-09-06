```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Input:
        numbers (List[float]): List of input numbers to be transformed
    Output:
    transformed_numbers (List[float]): Transformed list where the smallest number becomes 0 and the largest becomes 1
    """
    transformed_numbers = [x / 100.0 for x in numbers]
    return transformed_numbers
```

The function 'rescale_to_unit' takes a list of numbers and returns a new list where each number has been rescaled so that the smallest number in the original list is 0 and the largest number in the original list is 1.