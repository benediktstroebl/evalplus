```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    return (x, coeff) = the first item of the list
    x = x + 1
    coef = poly(xs) / poly(xs[:-x+1])
    return x, coef
```

This script defines two functions: `poly` and `find_zero`. The `poly` function computes the polynomial value for a given set of coefficients. The `find_zero` function determines the zero of a polynomial using the `poly` function.  The function then takes a list of coefficients and returns the zero of the polynomial with those coefficients.