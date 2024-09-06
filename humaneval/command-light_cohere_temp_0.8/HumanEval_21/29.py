```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    numbers = [x / max(numbers) for x in numbers if x != 0]
    return [x * max(numbers) if x != 0 else x for x in numbers]

def test_rescale_to_unit():
    assert rescale_to_unit([1.0, 2.0, 3.0, 5]) == [ [0.0, 0.0, 0.0, 0]
   6]
    assert rescale_to_unit([0.0, 0]) == [0.0, 0]

def test_rescale_to_unit2():
    assert rescale_to_unit([1.0, 2.0]) == [ [ [0.0, 1.0, 1]

def test_rescale_to_unit3():
    assert rescale_to_unit([-1.0, -2.0]) == [-0.0, 0.0, -1.0]

def test_rescale_to_unit4():
    assert rescale_to_unit([0.0, 0]) == [0.0, 0]

def test_rescale_to_unit5():
    assert rescale_to_unit([4.0, 0]) == [1.0, 0]

def test_rescale_to_unit6():
    assert rescale_to_unit([6.0, 0]) == [1.0, 0]
```
This Python code defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a rescaled list where the smallest number is 0 and the largest number is 1. The function achieves this by dividing each number in the list by the maximum value of the numbers, which results in dividing the numbers by 0 and scaling them up by 1. The test functions at the import the `rescale_to_unit` function and check that the function returns the expected results for different input lists.