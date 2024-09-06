```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Input:
    numbers: list of float, with at least two elements.

    Output:
    Rescaleded numbers in the list, such that the smallest number becomes 0 and the largest becomes 1.

    Test case:
    >>> test_list = [1.0, 2.0, 3.0, 4.0, 5]
   0
    [1.0, 2.0, 0]

    Test that the smallest number in test_list is 1.0, the second smallest number should be 0.0
    Test that the list is [1.0, 0.0, 3.0, 1]
    Output: [0.0, 0.0, 1.0, 0.0]
    - Test that second element of the list is unchanged, which means the function works correctly.