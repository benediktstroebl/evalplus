Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation
    numbers = [x / (x + 1.0) for x in numbers]
    # Return the rescaled numbers
    return numbers

def test_rescale_to_unit(test_numbers):
    actual_numbers = rescale_to_unit(test_numbers)
    assert actual_numbers == [0.0, 0.0, 0.0, 0.0, 0.5]
   0
0.
```
In this script, the `rescale_to_unit` function takes a list of numbers and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. The function then returns the numbers.

The `test_rescale_to_unit` function tests the `rescale_to_unit` function with a list of numbers and asserts that the actual output is equal to the expected output.