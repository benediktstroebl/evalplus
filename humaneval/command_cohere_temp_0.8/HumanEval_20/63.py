```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must have a length of at least two")
    else:
        middle = len(numbers) // 2
        return numbers[middle], numbers[-1]
```

This script defines a function `find_closest_elements` which takes in a list of float numbers and returns two floats that are closest to each other from the list and are returned in order (smaller number, larger number). The script returns `None` if the list contains less than two numbers. The function works by first sorting the list of numbers, then checking if the list contains less than two numbers and if it does, raising an error. If the list contains two or more numbers, the function returns the middle number and the last number of the list (assuming the list has been sorted from smallest to largest). It assumes the list is already sorted in `asc` order.

Here is a simple test suite for this function:
```python
import unittest

def test_find_closest_elements():
    # Act
    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])

    # Assert
    assert result == (2.0, 2.2)

    result = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    assert result == (2.0, 2.0)

    # Edge case
    with unittest.assertRaises(IndexError):
        find_closest_elements([1.0, 2.0])

test_find_closest_elements()
``` 
This test suite includes a variety of tests to validate the function in different cases:
1. Valid input with closest numbers.
2. Valid input with a single number list, which should throw an error. 
3. A test that asserts the function raises an `IndexError` when it is called with a list of size 1. 
4. The `test_find_closest_elements` function runs the tests and expected exceptions, using the `unittest` module.  It checks if the function returns the correct closest elements and raises the expected IndexError when the list contains less than two elements.  The `unittest` module provides a `main` function that runs all the defined test functions when the script is run. 

Note that, this code assumes the list is already sorted, and the solution would vary if that wasn't the case.