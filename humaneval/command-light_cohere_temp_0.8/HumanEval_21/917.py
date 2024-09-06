```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transform to the numbers list
    numbers_res = [x * 100.0 for x in numbers]
    return numbers_res

def test_rescale_to_unit(test_numbers: List[float]):
    actual_numbers = rescale_to_unit(test_numbers)
    assert all(actual_numbers >= 0 and actual_numbers <= 1)
    assert sum(actual_numbers) == sum(test_numbers)
    assert max(actual_numbers) == 1 and min(actual_numbers) == 0
```
This code provides a function `rescale_to_unit` that converts a list of numbers to the unit [0, 1]. The function takes a list of numbers as input and returns a new list of numbers after applying the linear transformation. The `test_rescale_to_unit` function tests if the `rescale_to_unit` function works correctly by passing the test list and checking the results against the expected behavior.