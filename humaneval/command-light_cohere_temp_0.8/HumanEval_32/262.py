```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    ensure that xs have even number of coefficients, and largest non zero coefficient as it guarantees
    a solution.
 }
    x = xs[0] / xs[1] ** (xs[1] ** 2 - 4 * x) ** 2
    return x
```
The function `find_zero` takes in a list `xs` of coefficients of a polynomial, and returns the value of the first zero of the polynomial `poly(x)` at x `x`.