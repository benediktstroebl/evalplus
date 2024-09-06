```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients xs. """
    n = len(xs) - 1
    deriv = [0] * n
    x = 1
    for i in range(n):
        deriv[i] = xs[i+1] * x
        x *= x
    return deriv
```

To test the above function, we can define a simple testing module:
```python
import unittest
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([0, 0, 0, 0]) == [0, 0, 0, 0]

class TestDerivative(unittest.TestCase):
    def test_derivative(self):
        test_derivative()

if __name__ == '__main__':
    unittest.main()
```

When you run the testing module, the `TestDerivative` class will execute the `test_derivative()` function, which verifies if the output of `derivative()` matches the expected result. 

Note, the test case for the edge case of an empty list ([0, 0, 0, 0, 0]) was added to cover a scenario where the derivative of a constant function is zero. 

The function and test module together provide a self-contained solution to the problem as asked.