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
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    None is a only valid form for polynomial zeroes
    """
    return None if len(xs) == 0 else round(find_zero(xs), 2)

xs = [1, 2]
x = 0.5
print(poly(xs, x))
print(find_zero(xs))
```
The function poly evaluates a polynomial with coefficients xs at the point x. The function find_zero finds the zero of the polynomial poly(x) by computing its values at every point x. 
The script then creates a list of coefficients and evaluates the polynomial and finds the zeroes at x = 0.5.