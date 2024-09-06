```python
def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 2
    return result
```

To test the script, we can create a test module or reuse existing test frameworks, such as the built-in `unittest` that comes with Python.

You can then run the tests individually by invoking the `unittest` module or using an IDE/shell that supports test discovery to run all tests in the module. 

The test code provided earlier looks like this:
```python
import unittest

class TestDerivative(unittest.TestCase):
    def test_deriv_basic(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_deriv_edge_case(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_deriv_multiple_x(self):
        self.assertEqual(derivative([2, 3, 4, 5, 6]), [4, 12, 20, 30])

    def test_deriv_zero_edge_case(self):
        self.assertEqual(derivative([0, 0, 0, 0]), [0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()
```
This script encapsulates each test in a separate function for clarity and readability, making it easier to identify and modify tests as needed. 

The `unittest.main()` call executes the tests when the script is run directly. 

To run the tests, ensure the Python test runner is installed (`pip install unittest`) and then execute the `test_derivative.py` script file. You can do this in your Python environment or IDE, which will run the tests and report any failures or errors. 

This way, you can ensure that the `derivative` function operates correctly and passes all the tests, providing confidence in its correctness.