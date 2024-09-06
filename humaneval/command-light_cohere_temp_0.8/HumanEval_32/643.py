```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution (from calculus).
    def test(xs: list):
    """
    Test the coefficients of a polynomial
    test returns True if the polynomial is the zero polynomial, and False otherwise
    """
    return all(c == 0 for c in xs) and xs[-1] == 0

xs = [1, 2]
test(xs)  # True
``` 
This script defines a function test that tests the coefficients of a polynomial to determine if it is the zero polynomial. The function test returns True if all the coefficients are zero and the last coefficient is zero, indicating the polynomial is the zero polynomial.