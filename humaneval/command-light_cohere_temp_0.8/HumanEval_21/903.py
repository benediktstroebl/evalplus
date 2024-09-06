```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    :
    numbers
    list of numbers with a minimum of 0 and a maximum of 1.

tests:
    """
    Test 1:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
        [[0.0, 0.0, 0.0, 0]]
    Test 2:
        >>> rescale_to_unit([0.0, 0.0, 0])
        [[0.0, 0.0, 0]]
    Test 3:
        >>> rescale_to_unit([0.0, 0, 0])
        [[0.0, 0.0, 0]]
    Test 4:
        >>> rescale_to_unit([0.0, 0, 0, 0])
        [[0.0, 0.0, 0]]
    Test 5:
        >>> rescale_to_unit([0.0, 0, -0.0])
        [[0.0, 0.0, 0]]
    Test 6:
        >>> rescale_to_unit([0.0, 0, 0, -0.0])
        [[0.0, 0.0, 0]]
Test 7:
        >>> rescale_to_unit([0.0, 0, 0, 0, 0])
        [[0.0, 0.0, 0, 0]]

The solution in this case is a linear transformation of the form [x,y] = [a,b] where a,b are any real numbers.  The input to the function should be a list of numbers with at least two elements, and the output will be a list of numbers with a minimum of 0 and a maximum of 1.