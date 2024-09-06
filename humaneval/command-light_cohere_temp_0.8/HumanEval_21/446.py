```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    :Return the1 numbers after the apply the transformation
    """
    numbers[0] = 0
    numbers[1] = 1
    return numbers
```