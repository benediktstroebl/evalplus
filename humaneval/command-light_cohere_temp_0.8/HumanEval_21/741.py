```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    Test: Test with the input numbers [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    expected ( list must be in order [0.0, 0.0, 0.0, 0.0, 0.5]
    first element [return list to be in order [0.0, 0.0, 0.0, 0.0]
Test with input numbers [1.0, 2.0, 3.0, 4.0, 5] using the1 in the test)
    Test: Test with input numbers [1.0, 1.0, 2.0, 4.0, 5]
   1 in the test)
    Test: Test with input numbers [1.0, 0.0, 0.0, 0.0, 6] using list [0.0, 0.0, 0.0] and be in order in the test.