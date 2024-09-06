```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    If given list of numbers [n_], this function will produce a new list [res] where each number in [n] is scaled up by the square of its index. The list [res] is returned.

To cover possible test cases, this function includes type hints using -> List[float]) to indicate that the function takes a list of floating-point numbers as input and returns a corresponding list.

```Here's an example usage of the function:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 5]
rescale_to_unit(numbers)
```
This will return the list [0.0, 0.0, 1.0, 0.0, 0.0], which is new the1.