```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digits."""
    return sorted(x for x in xs if not any(int(d) % 2 == 0 for d in str(x)))
```

The problem is solved in Python 3.8 and above with the help of a generator expression. A generator expression is a way to create a list in memory that is more efficient when dealing with large datasets. The generator expression `x for x in xs if not any(int(d) % 2 == 0 for d in str(x))` creates a list of all the elements in `xs` that have no even digits in their representation. As a list is returned, it is automatically sorted in increasing order. 

The tests are performed with the help of the Python function `assert`. It provides a way to check whether a given value meets a certain condition, and if the condition is not met, assert raises an AssertionError. In the case of the generator expression, it is helpful to use a list comprehension to evaluate the generator for test purposes, e.g. `[x for x in xs if not any(int(d) % 2 == 0 for d in str(x))]`). 

The following is an example of a test case for the function `unique_digits`:
```python
import unittest

class TestUniqueDigits(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

    def test_empty(self):
        self.assertEqual(unique_digits([]), [])

    def test_with_duplicates(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1, 15, 33]), [1, 15, 33])

 if __name__ == '__main__':
    unittest.main()
```

In the test suite, the function `unittest.main()` serves as an entry point to run all tests. The `TestUniqueDigits` class inherits from `unittest.TestCase`, providing a container for each individual test case. For each test, `assertEqual` is used to compare the output of the function `unique_digits` against the known correct value in the test case. If the values do not compare equally, the test fails. 

To run the test file, you need to execute the file directly or put it in a Python module and run it with the `python -m unittest discover` command.