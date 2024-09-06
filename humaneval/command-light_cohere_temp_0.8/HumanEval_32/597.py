```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * *math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    ensure even number of coefficients
    """
    find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
   
    test cases:
    assert poly(xs=[1, 2], x=1) == 1 + 2
    assert poly(xs=[-6, 11, -6, 1]) == -6 + 11x - 6x^2 + x^3
    assert poly(xs=[1, 2, 3]) == 1 + 2x + 3x^2
    assert poly(xs=[-1, -2, -3]) == -1 - 2x - 3x^2
    assert poly(xs=[-6, 11, -6]) == -6 + 11x - 6x^2

This script defines a function that calculates the polynomial with a given list of coefficients, and a function that finds the zero of a polynomial with a given list of coefficients.