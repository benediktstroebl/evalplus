```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    # Initialize variables
    min_val = min(numbers)
    max_val = max(numbers)
    # Apply the transformation
    numbers = [x / (max_val - min_val) if abs(x - min_val) <= max_val - min_val else x - min_val for x in numbers]
    # Return the transformed list
    return numbers
```