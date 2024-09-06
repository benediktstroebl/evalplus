```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    : - Test case 1:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
    expected output [ [0.0, 0.0, 0.0] )

    test case 2:
    >>> rescale_to_unit([0.0, 5.0, 10.0])
    expected output [ [0.0, 0.0, 0.0] )
    added_values are:
    Test case passed successfully!