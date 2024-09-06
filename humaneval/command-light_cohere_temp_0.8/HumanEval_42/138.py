```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l[:] = [i+1 for i in l]
    return l

# Test suite using built-in unittest module
import unittest

class IncrListTestCase(unittest.TestCase.TestCase)
def test_incr_list():
    """Test suite for IncrList function."""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    incr_list(lst)
    lst2 = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert lst == lst2
    return_result()

if __name__ == '__main__':
    unittest.run('test_incr_list')
```
The function `incr_list` takes a list as input and returns a new list with elements incremented by 1. The test suite `test_incr_list` contains a series of test cases that verify the correctness of the `incr_list` function.  The test suite using the Python's `unittest` module.  By calling `unittest.run('test_incr_list')`, the test suite is executed, and the program prints the test results.