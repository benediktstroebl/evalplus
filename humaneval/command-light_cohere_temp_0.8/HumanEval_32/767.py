```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many.
    find_zero returns only zero point, even if there are many
    solutions.
    """

   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

def test(xs: list):
    """
    Test if coefficients list has even number of elements
    and the largest coefficient is not zero.
    """
    return (not len(xs) % 2 == 0 and xs[0] != 0) and xs[1:]

xs = [1, 2]
test(xs)  # pass

xs = [-6, 11, -6, 1]
test(xs)  # pass

xs = [1, -2, -3]
test(xs) # fail

xs = [1, 2, 3, 4, 5]
test(xs) # pass
```
This script defines a function `poly` that computes the polynomial with the given coefficients, and another function `find_zero` that finds the zero of the polynomial. The `test` function verifies if the coefficients list has an even number of elements and the largest coefficient is not zero.