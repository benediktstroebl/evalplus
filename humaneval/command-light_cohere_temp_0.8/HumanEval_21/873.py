```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test Cases: [0.0, 0.0, 0.0, 1.0, 0.0, 0.0]
   0.0, 0.0]

   0.0, 0.0, 2.0, 0.0]
    return_list.
    [2.0, 0.0, 0.0, 1.0]
   0.0, 2.0]
   0.0, 0]
   1.0]
   0.0, 0]
   0]
    [0.0, 3.0, 2.0, 0]

    new_list = rescale_to_unit([0.0, 3.0, 2.0, 0])
    return [1.0, 0.0, 0]
new_list
```