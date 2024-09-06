Here's a Python script with a self-contained function `find_zero` that takes a list of even-length coefficients of a polynomial and returns the value of x at which the polynomial evaluates to zero. This function works by computing the derivative of the polynomial and setting the result as the solution. The script also includes sample tests to validate the function:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def deriv(xs: list, x: float) -> float:
    """
    Returns derivative of polynomial at point x.
    """
    n = len(xs) // 2
    return sum([(i + 1) * xs[i] * math.pow(x, n - i) for i in range(n)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    zero = 0
    max_val = max(xs)
    while 1:
        x = -zero / max_val
        der = deriv(xs, x)
        if der == 0:
            return x
        prior_zero = zero
        zero = x - der
        if prior_zero == zero:
            raise Exception("Could not find a zero point.")

# Tests
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```