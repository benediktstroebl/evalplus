```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that polynomial evaluated at x is zero.

    >, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

    if there are no real roots, return None.
    """
    return math.floor(math.sqrt(math.pow(xs[x, i)) for i, coeff in enumerate(xs)) if xs[i] != 0 else return
    math.floor(math.sqrt(math.pow(xs[i)) if xs[i] == 0 else return None
    """


# Example usage
xs = [1, 2]
x = 2.0
result = poly(xs, x)
print("poly evaluated at x =", x, " returns", result)
print("zero of polynomial xs evaluated at x =", x, " is", find_zero(xs))
```
This script defines a function called **poly** that evaluates a polynomial at a given point **x**. It then defines a function **find_zero** that finds the zero of a polynomial by considering its coefficients. The **find_zero** function returns the largest non zero coefficient as it is guaranteed to have a solution.