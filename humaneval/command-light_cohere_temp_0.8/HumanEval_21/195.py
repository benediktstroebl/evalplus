```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   0. 
    numbers = [rescale_to_unit(numbers)
    return numbers

def rescale_to_unit_test():
    """ Test function that passes the test suite for rescale_to_unit.
    input = [List[1.0, 2.0, 3.0, 4.0, 5])
   0.0, 0, 0]

    expected = [0.0, 0.0, 0.0, 0]
   
    actual = rescale_to_unit(input)

    assert expected == actual

rescale_to_unit_test()
```
This script defines a function called `rescale_to_unit` that takes a list of numbers and returns a new list with the numbers in a rescaled format. The `rescale_to_unit_test` function tests the `rescale_to_unit` function by passing in a test list and comparing the expected output with the actual output. 

This test ensures that the `rescale_to_unit` function correctly scales the input list of numbers.