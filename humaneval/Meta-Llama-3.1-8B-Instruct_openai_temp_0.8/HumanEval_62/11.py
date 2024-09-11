### Derivative of Polynomial Function in Python
#### Using Sympy Library for Symbolic Mathematics

```python
import sympy as sp

def derivative(xs: list):
    """
    Compute the derivative of a polynomial given its coefficients.

    Args:
        xs (list): Coefficients of the polynomial in descending order of powers.

    Returns:
        list: Derivative of the polynomial in the same form.
    """
    x = sp.symbols('x')
    polynomial = sum(coeff * x**i for i, coeff in enumerate(xs))
    derivative_polynomial = sp.diff(polynomial, x)
    return list(derivative_polynomial.as_coefficients_dict().values())

# Example usage:
print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # Output: [2, 6]
```

This script uses the `sympy` library to work with symbolic mathematics. It defines a function `derivative` that takes a list of coefficients as input, constructs a polynomial using these coefficients, computes the derivative of the polynomial using `sympy.diff`, and returns the coefficients of the derivative polynomial. The example usage at the end demonstrates the function's behavior with two different inputs.