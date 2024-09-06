```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and it finds zero using the maximum polynomial
    and takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    """
    -2> Round the output to 2 decimal places
    return round(find_zero([1, 2]), 2)
    -0.5
    -3> Compute and return the x-value corresponding to the zero polynomial
    -4>x**2+2*x+1

Your solution has passed all tests.