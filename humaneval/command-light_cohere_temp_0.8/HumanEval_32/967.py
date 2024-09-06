```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * *x_N) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    and, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

```

The function `find_zero` finds the zero of a polynomial represented as `poly` function. It uses the formula that for polynomial `poly` (x) = 0, the derivative `poly'(x)` = 0. The function then checks if the derivative is zero at the given `x` and returns the corresponding `x` value.

The function also uses the condition that the polynomial has at least 2 coefficients to guarantee the existence of a solution. This is done to ensure that the function will only return a valid answer, avoiding infinite loops.

The function also uses the `enumer` for the list of coefficients to iterate and calculate the polynomial's sum. The `math.pow` function is `i` for the `i` in the list to calculate the corresponding coefficient.