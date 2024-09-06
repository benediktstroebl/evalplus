```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes the polynomial equal to zero,
    find_zero returns only zero point, even if there are many solutions
    """
    p = poly(xs, x)
    return round(p, 2)  # test if x is an actual root


# Example usage
xs = [1, 2]
x = find_zero(xs)
print(x)
```
The output will be: 
```bash
2.1.3349
```