```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test:
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.5])
    low
    receive a input, output should be [0.0, 0.75, 1.5]
   0.5]
    then values that a well case of this function, as the input list should be numbers of at least two elements.  """ Output:
    [0.0, 0.0, 0.5]
    previous test test be a expected output and is correct.