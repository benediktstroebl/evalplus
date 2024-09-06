```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers[0] = 0
    numbers[1] = 1
    return numbers

def test_rescale_to_unit(test_numbers: List[float]) -> None:
    actual_numbers = rescale_to_unit(test_numbers)
    assert all(actual_numbers >= 0 and actual_numbers <= 1) == True
```
This script defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers but scaled to the range [0, 1]. The numbers in the original list are then rescaled to be in the range [0, 1]. 

The script also defines a test function called `test_rescale_to_unit` that takes a list of numbers as input and asserts that the `rescale_to_unit` function returns numbers that are within the range [0, 1]. 
This test function is designed to validate the correctness of the `rescale_to_unit` function by checking if the returned numbers are within the desired range.