```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes polynomial (xs)(x) = 0
    find_zero returns only zero point, even if there are many.
    None, None of the following cases:
    - xs is empty
    - xs has an odd number of coefficients
    - largest non zero coefficient is less than 0
    - largest non zero coefficient is not one
    """
    if len(xs) == 0:
        return None
    elif len(xs) % 2 == 1:
        return None
    else:
        x = float(xs[0])
        for coef in xs[1:]:
            if coef > 0 and x == coef:
                break
            elif coef < 0 and x == -coef:
                break
            elif coef == 0 and x == 0:
                return x
        return None
```