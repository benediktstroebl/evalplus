```python
def add(x: int, y: int):
    return x + y
```
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add(2, 3), 5)

    def test_other(self):
        self.assertEqual(add(5, 7), 12)
```

In the above code, the `add()` function takes two arguments, `x` and `y`, and returns their sum. The `TestAddFunction` class contains two test methods that exercise the `add()` function. The first test method, `test_basic`, verifies the function's correctness when adding 2 and 3, and the second test method, `test_other`, verifies the function's correctness when adding 5 and 7. 

When the `python test_add.py` command is run, the test suite will be executed, and any assertions within the test methods will be evaluated. If all tests pass, you will see an indication that the tests were successful. If any assertions fail, you will see an informative error message detailing which tests did not pass and what values were expected versus what was actually observed.