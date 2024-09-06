```python
def add(x: int, y: int):
    return x + y
```
```python
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_positive_numbers_second_case(self):
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
```
The provided code includes the `add` function and a set of unit tests that verify its correctness. In the `add` function, two parameters, `x` and `y`, are expected to be integers. It returns the sum of these two numbers using the `+` operator.

The test suite, comprised of two individual tests, is defined next. Each test case employs the `assertEqual` method from the `unittest` module. This method checks if the actual output from the `add` function matches the expected output for the given inputs.

To execute the test suite, the `unittest.main()` function is called at the end of the script. When the script is launched, this function instigates the running of all defined tests. If all tests pass, an indication of a successful test run will be provided. If any tests fail, detailed information on the nature of the failure will be presented.