```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x, returns sum of the coefficients
    """
    return sum([math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0, returns only zero point, even if there are many
    """
    return math.floor(find(poly, xs))
```
The above script defines a function `poly` that evaluates the polynomial at a given point `x`, and a function `find_zero` that finds the zero of the polynomial.