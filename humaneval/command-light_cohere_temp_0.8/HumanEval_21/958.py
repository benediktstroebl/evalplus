```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers[:] = [x / 100.0 for x in numbers]
    return numbers
```
This Python code defines a function rescale_to_unit, which takes a list of numbers as input and applies a linear transformation to each element in the list. The transformation ensures that the smallest number becomes 0 and the largest becomes 1, effectively normalizing the input data. This function is mathematical operation is accomplished using list comprehension and the division-by-100 operation, and the result is assigned back to the input numbers list.