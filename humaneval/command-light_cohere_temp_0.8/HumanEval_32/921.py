```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns the roots of the polynomial, which may be repeated or complex numbers.
    """
    find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    """
    return [*math.powi(math.pi) / math.sqrt(max(abs(xs))
```

This script defines a function that takes in a list of coefficients and a point x as input, and returns the polynomial evaluation at the given point x. It also defines a function that takes in a list of coefficients as input, and returns the roots of the polynomial, which may be repeated or complex numbers. The function uses the power series expansion to evaluate the polynomial, and uses the math library to calculate the roots of the polynomial.