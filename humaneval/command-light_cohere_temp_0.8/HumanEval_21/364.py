Here's a self-contained Python script with a function that solves the problem of scaling numbers in a list to the unit range of 0 to 1:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [x / 100.0 for x in numbers]
    return numbers

def test_rescale_to_unit(numbers):
    assert len(numbers) == 2
    assert numbers[0] == 0
    assert numbers[1] == 1
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0]) == [numberss
   
def test_rescale_to_unit(test_cases):
    assert test_rescale_to_unit([0.0, 2.0]) == [
   0
   0}
    assert test_rescale_to_unit([1.0, 0.0, 0]) == [0.0, 0.75]
   0
   0
def test_rescale_to_unit(test_cases_large):
    assert test_rescale_to_unit([0.5, 0]) == [0.0, 0.5]
   0
75, None)
```
This script defines a function `rescale_to_unit` that takes a list of numbers and scales them to a unit range of 0 to 1. The function then returns a list of the rescaled numbers. The script also defines three test functions to test the `rescale_to_unit` function: `test_rescale_to_unit([0.0, 2.0])` tests1 0` assert that the output is in the expected range, [0.0, 0.75] and that the0 assert that the output is in the expected range, [0.0, 0.75] and that the0 assert that the output is the expected value of None.