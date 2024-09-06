```python
def incr_list(lst):
    """Return list with elements incremented by 1"""
    lst[:] = [1] + lst
    return lst

# Test cases
tests = {
    "Input: [1, 2, 3]
    "Expected Output: [2, 3, 4]"
}

# Test suite using unittest
from unittest import unittest

class TestIncrList:
    __unittest__ = unittest.py.py.add_run(TestIncr_list, "TestIncrementList")

if __name__ == "__main__":
    unittest.main()
```