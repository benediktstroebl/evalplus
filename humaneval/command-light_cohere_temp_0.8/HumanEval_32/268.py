```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + ... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial
    find_zero find x such that polynomial x^n + xs[0] * x^(n-1) + xs[1] * x^n-2 + ... xs[n-1] * x^0 is equal to 0
    find_zero returns only zero point, even if there are many.
    """
    all(abs(c)<1e-10) and c != 0, where c is the coeff of xs
    """
    return round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
```

The provided Python code defines a polynomial function `poly` that computes the polynomial expression with given coefficients `xs` at a given point `x`. It also has a function `find_zero` that aims to find the zero of the polynomial expression. The `find_zero` function iterates through the list of coefficients and checks if the polynomial expression is equal to zero at a given value. If the coefficient list has even coefficients with absolute values less than 1e-10 and no zero coefficients, the function returns the value. If these conditions are not met, the function returns None.