```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    numbers[:] = [x / 100.0 for x in numbers]
    return numbers
```
This function is designed to normalize the given list of numbers so that the smallest value becomes 0 and the largest value becomes 1.  It function takes input of a list of numbers and returns a new list with the same elements, but each value has been divided by 100.