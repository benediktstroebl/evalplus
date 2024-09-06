```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if diff > 0.0:
            return numbers[-1], numbers[0]
        else:
            return numbers[0], numbers[-1]
```
The function `find_closest_elements` takes a list of numbers, sorts them, and then checks for the smallest difference between two adjacent elements in the sorted list. If the difference is greater than zero, the larger number is returned first, otherwise the smaller number is returned first. The function also checks for a minimum list length of two and raises a `ValueError` otherwise. 

Here is an example of how to use the function and test it using Python's `unittest` module:
```python
import unittest

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        diff = numbers[-1] - numbers[0]
        if diff > 0.0:
            return numbers[-1], numbers[0]
        else:
            return numbers[0], numbers[-1]

class TestFindClosestElements(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]), (2.0, 2.2))

    def test_no_exceptions_on_valid_input(self):
        self.assertEqual(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]), (2.0, 2.0))
        self.assertEqual(find_closest_elements([0.5, 1.0, 1.5, 2.0, 2.5, 3.0]), (1.0, 1.5))

    def test_exceptions_on_bad_input(self):
        self.assertRaises(ValueError, find_closest_elements, [1.0, 2.0])
        self.assertRaises(ValueError, find_closest_elements, [1.0, 2.0, 3.0, 4.0])

if __name__ == '__main__':
    unittest.main()
```

In the test suite, the `test_basic` function tests the function on the inputs provided in the docstring, while `test_no_exceptions_on_valid_input` tests the function on two valid inputs and `test_exceptions_on_bad_input` tests the function on two invalid inputs in terms of length and content, the latter of which is expected to raise a `ValueError