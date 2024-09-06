```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *
   .pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.

    Test:
    1. ```
    1. Calculate poly(x)
    result of calling poly with list [1, 2, -3, -2, 4, 5, -6] and x = 1

    Answer: 1.0 + 2* x + (-3) * x^2 + (-2) * x^3 + 4 * x^4 + (-6) * x^5 = -1 + 2 * x - 3 * x^2 + 4 * x^3 - 6 * x^4 + x^5

    2. 0
    same result of finding a zero for this polynomial, as x = 1 satisfies this condition.
```