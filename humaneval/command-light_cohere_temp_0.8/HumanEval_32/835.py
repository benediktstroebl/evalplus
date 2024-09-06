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
    find_zero returns only zero point, even if there are many solutions
    and finds_zero only takes list xs having even number of coefficients and the largest non-zero coefficient as it guarantees a solution.
    """
    rounded version:
    return round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    def test(xs: list, x: float):
        return poly(xs, x)
    def find_zero(xs):
        # test if correct number of coefficients
        if len(xs) % 2 != 0:
            raise ValueError("list must have even number of coefficients")
        # find largest coefficient
        max_coeff = max(xs)
        # find value that makes polynomial zero
        for x in range(-max_coeff, max_coeff):
            if poly(xs, x) == 0:
                return x
        return None
```