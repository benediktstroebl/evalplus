Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    min_val = min(numbers)
    max_val = max(numbers)
    return [((x - min_val) / (max_val - min_val)) for x in numbers]
```
The function `rescale_to_unit()` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1. The transformation is a linear normalization that scales the numbers between 0 and 1. 

You can test this function with the provided test case:
```python
test_rescale_to_unit = [(1.0, 2.0, 3.0, 4.0, 5.0,), 
                        (0.5, 1.5, 2.5, 3.5, 4.5,)]

for test_case in test_rescale_to_unit:
    assert rescale_to_unit(test_case) == [0.0, 0.25, 0.5, 0.75, 1.0]
```
The `assert` statement verifies if the output of the function corresponds to the expected output for the input test case. 
This script ensures the function `rescale_to_unit()` works correctly and maintains the smallest number at 0 and the largest number at 1, regardless of the input list.