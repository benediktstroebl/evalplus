```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test:
    print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.5, 0])
   
    """ List[int] [0.0, 0]
    numbers, apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0]) == [ [0.0, 0, 1.0] )
assert rescale_to_unit([0.0, 0]) == [0.0]
assert rescale_to_unit([1.0, 0, 0]) == [0.0]
assert rescale_to_unit([0.0, 0.0, 0]) == [0.0, 1.0]

assert rescale_to_unit([0.0, 0, 0]) == [0.0, 1.0]
assert rescale_to_unit([1.0, 2.0, 3.0]) == [List([0.0, 0.0, 0])
assert rescale_to_unit([1.0, 2.0, 3.0]) == [[0.0, 1.0, 0]
assert rescale_to_unit([1.0, 2.0, 3.0]) == [List([0.0, 0, 0.0])
assert rescale_to_unit([1.0, 2.0, 3.0]) == [[0.0, 1.0, 0]
```