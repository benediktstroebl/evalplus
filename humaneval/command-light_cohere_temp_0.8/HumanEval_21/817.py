Here's the provided self-contained Python script:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers[0] = 0
    numbers[1] = 1
    return numbers

def test_rescale_to_unit(numbers: List[float]):
    """
    Test function to check if the rescale_to_unit function works correctly on a given list
    """
    original = [1.0, 2.0, 3.0, 4.0]
   0
    test if the can be successfully transformed to [0.0, 0, 0.0, 1.0], which is

    original = [0.0, 0.0, 0.0, 1.0]
   6 a expected transformation,
    fail.
```
The function `rescale_to_unit` in this script accepts a list of numbers as an argument and modifies the list according to a linear transformation that scales the values from 0 to 1 and shrinks them to 0. The test function `test_rescale_to_unit` is used to test the `rescale_to_unit` function with a sample list of numbers.