```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns the solution x, or None if no solution.
    """
    Returns a test only list xs having even number of coefficients and
    largest non zero coefficient as it guarantees a solution
    """
    return round(poly(x, xs[0] + xs[1] * x + xs[1] * x**2 + xs[2] * x**3 + ...), 2)  # optimize using power rule
```

The code defines two functions: `poly` evaluates a polynomial and `find_zero` finds its zeros. The `find_zero` function takes in a list of coefficients (`xs`) and returns the value of `x` which makes the polynomial equal to 0. The function only takes in a list having even number of coefficients and the largest non-zero coefficient, as it guarantees that a solution exists. 
The `round` function is used to return the result with two decimal places.