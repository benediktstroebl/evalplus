```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial represented by its coefficients.
    
    Args:
        xs (list): List of coefficients of the polynomial, in the order: xs[0] + xs[1] * x + xs[2] * x^2 + ...
    
    Returns:
        list: List of derivatives for each term.
    """
    result = []
    x = 1
    for xi in xs:
        result.append(xi * x)
        x *= 1 + 1j if len(xs) > 1 else 1
    return result
```

The function takes a list `xs` as input, which represents the coefficients of a polynomial, and returns a list of the derivatives of each term in the polynomial. The function also includes a docstring and type annotations for better readability and usability.

To test the function, you can use the following Python code:
```python
import unittest

class TestPolynomialDerivative(unittest.TestCase):
    def test_derivative_simple(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_with_constant_term(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_derivative_with_complex_coefficients(self):
        self.assertEqual(derivative([3 + 2j, 4 - 3j, 5 + 6j]), [3 - 2j, 13 - 3j, 65 - 6j])

if __name__ == '__main__':
    unittest.main()
```

This test suite includes three test cases: one for a simple polynomial, one for a polynomial with a constant term, and one for a polynomial with complex coefficients. The `derivative` function is applied to a list of polynomial coefficients, and the result is compared to the expected list of derivatives.