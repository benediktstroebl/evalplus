```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Input: numbers: list[float] - list of numbers to be rescaled
    Output: list[float] - list of rescaled numbers, where 0 is the smallest and 1 is the largest number.

    Test case:
        1.0 - biggest element
        test
        2.0 + smallest element and100 to be the same, as it should be
    """
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   0
    test out numbers.lprint()
        x: [0.0, 0.0, 0.0] = [0.0 / numbers"result
   0 in the list
    # make sure numbers are sorted in ascending order
        return numbers[::-1]  # slice the list in reverse order and convert to list[float]