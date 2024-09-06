```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    # test: verify that list xs has even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients must have even length")
    # sort xs by coefficients, so that the coefficient with the largest absolute value comes first
    xs.sort( key=lambda coeff, abs(co) )
    # compute coefficients of x^0
    x_0 = xs[0] / math.pow(x, x_0)
    # compute coefficients of x^1
    x_1 = xs[1] / math.pow(x, x_0)
    # compute coefficients of x^2
    x_2 = xs[2] / math.pow(x, x_0)
    # compute coefficients of x^3 and beyond
    for i in range(3, len(xs)):
        x_i = xs[i] / math.pow(x, x_0)
    # compute polynomial
    p = x_0 + x_1 * x + x_2 * x**2 + x_3 * x**3 + ...
    # evaluate polynomial at x = 0
    # verify if the polynomial is equal to 0
    if poly(xs, 0) != 0:
        raise ValueError("The coefficients do not produce a non-zero polynomial")
    # verify if the polynomial is equal to 1 (or -1)
    if poly(xs, 1) != 0:
        raise ValueError("The coefficients do not produce a non-zero polynomial")
    # verify if the polynomial is equal to x^2 (or -x^2)
    if poly(xs, 2) != 0:
        raise ValueError("The coefficients do not produce a non-zero polynomial")
    return x_0


# Example:
xs = [1, 2]
x = find_zero(xs)
print(x)
```