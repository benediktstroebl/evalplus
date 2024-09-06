Here is a self-contained Python script that solves the problem you described:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n / (n + 1)) for n in numbers
    """
    
    assert all(numbers >= 0)
    assert all(numbers <= 1)
    return numbers
```