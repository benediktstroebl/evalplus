```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and it finds_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

xs = [1, 2]
x = find_zero(xs)
print(f'x={x}')
``` 
This script defines a function `poly` that evaluates a polynomial with coefficients `xs` at a given point `x`. The function `find_zero` finds the zero of the polynomial with coefficients `xs`.