```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test:
    test_rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
   0.0, 0]
   a
 Rescale values to the unit:
    Test2:
    test_rescale_to_unit([0.01, 1.0, 0])
   >
    Output:
    [0.0, 0.0, 0]