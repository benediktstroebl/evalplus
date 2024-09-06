Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1.

To test this function, you can use the following code:
```python
# Test code
import random
import pytest

@pytest.mark.parametrize('test_input, expected', [
    ([1.0, 2.0, 3.0, 4.0, 5.0], [0.0, 0.25, 0.5, 0.75, 1.0]),
    ([-5.0, -3.0, -1.0, 1.0, 3.0, 5.0], [-.25, -.08333, 0.0, .25, .75, 1.0])
])
def test_rescale_to_unit(test_input, expected):
    result = rescale_to_unit(test_input)
    for x, y in zip(result, expected):
        assert x == y
```
This test code uses the `pytest.mark.parametrize` function to test the `rescale_to_unit` function with two different input datasets, and expected output datasets. For each dataset, it compares each element of the input list with the corresponding element in the expected list, ensuring that they are equal.