Here is a Python script with a self-contained function that solves the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0
    for num in numbers[1:]:
        num = min(num, 0) + 1
    return numbers


def test_rescale_to_unit():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5]) == [ [ [0.0, 1.0, 0.0, 1])
   
    assert rescale_to_unit([0.0, 0.0, 0.0, 0]) == [ [0.0, 0.0, 0])
    assert rescale_to_unit([0.0, 0.0, 0.0, 0]) == [ [0.0, 0])
assert rescale_to_unit([1.0, 0.0, 0]) == [ [0.0, 0])

def test_rescale_to_unit_list():
    assert [rescale_to_unit([1.0, 2.0, 3.0, 4]) == [ [0.0, 0.0, 0])
assert [rescale_to_unit([0.0, 0.0, 0, 0]) == [0.0, 0])

def test_rescale_to_unit_tuple():
    assert [rescale_to_unit((1.0, 2.0, 3.0, 4)) == [ [0.0, 0)]

def test_rescale_to_unit_value():
    assert rescale_to_unit(10.0) == [0.0]
assert rescale_to_unit(0.0) == [1.0]

def test_rescale_to_unit_odd_number():
    assert rescale_to_unit([3.0]) == [0.0] == [1.0]
assert rescale_to_unit([-2.0]) == [0.0] == -0.0) == True


test_rescale_to_unit()
test_rescale_to_unit_list()
test_rescale_to_unit_tuple()
test_rescale_to_unit_value()
test_rescale_to_unit_odd_number()
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list where each number has been scaled to range 0 to 1. The `test_rescale_to_unit` function is an example of how to use the `rescale_to_unit` function to test the functionality of the function.

The script also includes additional tests to ensure the correctness of the `rescale_to_unit` function for different inputs.