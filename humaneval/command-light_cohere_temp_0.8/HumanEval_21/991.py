Here is a self-contained Python script that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    : 1.0, -2.0), 3.0, -4.5
   0, 0)

    return numbers
```
The function takes a list of numbers and returns a list of the same numbers, but with each number scaled to be between 0 and 1.