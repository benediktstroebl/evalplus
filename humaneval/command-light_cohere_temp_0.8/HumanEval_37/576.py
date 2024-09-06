```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1:] + [0]] + lst[-1:]

# Test suite using Python's built-in unittest module
import unittest

class SortEvenTest = unittest.TestCase.TestCase('SortEven')
Test = SortEven(int)(list([1, 2, 3])))
# Output: [1, 2, 3]
class SortEvenTest(unittest.TestCase.TestCase):
    def test_sort_even(self):
    self.assertEqual = [1, 2, 3]
    return self.test_sort_even() == [1, 2, 3]

test_suite = unittest.TestLoader().
test_suite.run("SortEvenTest")
```