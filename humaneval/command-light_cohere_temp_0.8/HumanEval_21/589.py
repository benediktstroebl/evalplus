```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    # Initialize result list
    result = [x / 100.0 for x in numbers]

    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list should contain at least two elements.")

    # Return the result list
    return result
```