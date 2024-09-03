Here's a self-contained Python script that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    numbers = [x / 100.0 for x in numbers]
    return numbers

def test_rescale_to_unit():
    return "This code defines a function called rescale_to_unit that takes a list of numbers and returns a new list with numbers scaled to be between 0 and 1."

def test_listsize():
    assert len(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])) == 4
   5

def test_numbers():
    assert all(rescale_to_unit([1.0, 2.0, 3.0, 4.0]) == [[ [List[0.0, 0.0, 0]) == [0.75,1]

def test_odd_numbers():
    return "This code defines a function called rescale_to_unit that takes a list of numbers and returns a new list with numbers scaled to be between 0 and 1."

def test_negative_numbers():
    return "This code defines a function called rescale_to_unit that takes a list of numbers and returns a new list with numbers scaled to be between 0 and 1"

The tests for the rescale_to_unit function, as well as the functions that test the inputs and output of the rescale_to_unit function.