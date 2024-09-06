Here is a self-contained Python script that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1"""
    numbers[0] = min(numbers)
    numbers[0] = max(numbers)
    return numbers
```