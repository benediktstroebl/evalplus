```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coefficient * math.pow(x, i) for i, coefficient in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and polynomial(x) = 0 is a linear equation in x.
    """
    return math.ceil(x) / math.floor(math.sqrt((xs[-1] **x **2) + 1e))
# note: only even if largest nonzero coefficient is 1, there is always exactly one solution
# f(x) = x**2 + 1 is a well known example of this
    #   fact, since x**2 + 1 = (x+1)*(x-1) and the above function
    #   factors the solution x-1/x-1.
# For, there are also other cases, but they are not as interesting as this one
    #   for our purposes
    #   (in fact, polynomial(x) = 0 has infinitely many solutions in
    #     the complex plane, but we'll ignore that for now)

# test cases
print(poly([1, 2], 2)) # [0] + [2] * x + [2] * x**2 = 4
print(poly([-6, 11, -6, 1], x)) # (-6) + [11] * x**3 + [1] * x**2 + [1] * x + 1 = 0
```