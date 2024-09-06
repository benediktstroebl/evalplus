```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

The function relies on the use of a generator expression, which allows for short-circuit logic and yields boolean value as soon as a true comparison is found. 

This approach is both more memory efficient and also executes slightly faster than a comparable list comprehension, because it doesn't require the entire list to be generated. 

The `any()` function then evaluates the generator expression for each element in the list, and returns True if any of the comparisons are true. 

Finally, the function returns False, if no comparisons are true for any elements in the list. 

You can test this function against the given test cases like so:
```python
import unittest

class TestHasCloseElements(unittest.TestCase):
    def test_has_close_elements_false(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_has_close_elements_true(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

if __name__ == '__main__':
    unittest.main()
```

This uses the `unittest` module to test the function.  Two test cases are defined, and the `unittest.main()` function is used to run the tests.  The output will then indicate whether the tests passed or failed.