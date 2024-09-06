```python
def get_positive(input_list):
    return [num for num in input_list if num > 0]

# Test suite using Python's built-in unittest module
import unittest

class TestPositiveNumbers = unittest.TestCase('get_positive')

# Test 1: Should return an list with only positive numbers?
test_positive_numbers1 = TestPositiveNumbers().wait()
test_positive_numbers1.checkers([-1, 2, -4, 5, 6])
test_positive_numbers1.checkPass("Should return a list with only positive numbers.")
```