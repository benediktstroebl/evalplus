Here's the self-contained Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
     # numbers >= 2.
    numbers = [[numbers - (x=0, x) for x in numbers]
    return numbers

def test_rescale_to_unit() -> None:
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 1.0]
   
assert rescale_to_unit([10.0, 5.0, 6.0]) == [numbers >= 2.0
```