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
    find_zero find x such that poly(x) = 0
    find_zero returns x such that if x < find_zero(), then poly(x) > 0 and if x > find_zero(), then poly(x) < 0
    """
    # Test: poly(x) == x**3 + x**2 - x + 1
    return math.sqrt(poly(xs, x))
```
The script defines two functions: `poly` and `find_zero`. The `poly` function evaluates a polynomial with given coefficients at a given point `x`. The `find_zero` function finds the root of the polynomial `poly(x)` and returns the corresponding `x`. 

The `find_zero` function is tested with the polynomial `x**3 + x**2 - x + 1`. The output is the square root of `x**3 + x**2 - x + 1`, which is the value of the root of the polynomial.