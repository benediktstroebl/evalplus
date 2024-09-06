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
    find_zero finds x that makes polynomial(x) = 0, returns only zero point, even if there are many,
    and finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    assert len(xs) % 2 == 0
    assert xs[0] > 0
    return math.floor(find_zero(xs))
```
The function finds the zero point of a polynomial by repeatedly applying the polynomial to a candidate value x and checking if the result is zero. The function then returns the maximum value of x that makes the polynomial zero, which is guaranteed to exist by the condition on the coefficients of the polynomial.