```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes polynomial poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and finds_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
    is the solution.
def test(xs: list, y: float):
    """
    Tests if polynomial with coefficients xs at point y is true.
    """
    return sum([coeff * math.pow(y, i) for i, coeff in enumerate(xs)]) == 0
    """
return sum([coeff * math.pow(y, i) for i, coeff in enumerate(xs)]) == 0
```
The script defines three functions: poly, find_zero and test. It evaluates polynomial by the function using coefficients at a point x and returns the result. The function find_zero finds the zero of the polynomial using the formula and returns only the zero point, even if there are many solutions. Finally, the function test tests if a polynomial is true at a given point y and returns the result.