```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Test:
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0.0])
   0.0, 0.0, 0.0
    Test
       0, 0]
    is output:

    Rescale_to_unit([0.5, 0.0, 0, 0.0, 0.5])
   
   0.0, 0.0, 0)
   is the following assertions are also True

    Test2:
    assert rescale_to_unit([1.0, 2.0]) == [[0.0, 0, 0.0, 1.0])
   0.0, 0)
   0.0, 0)

    Test3:
    assert rescale_to_unit([0.0, 0]) == [0.0, 0]
0.0, 0]
```