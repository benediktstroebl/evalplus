```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes polynomial(x) = 0, returns only zero point, even if there are many solutions.

    if xs has even list has even number of coefficients or if largest non-zero coefficient is less than tolerance, return None
    """
    n = len(xs)
    if n == 0:
        return None
    elif n == 1:
        return math.floor(xs[0])
    elif n == 2:
        return math.floor(xs[1]) * math.pow(xs[0], -x)
    elif n % 2 == 1:
        return math.floor(xs[1]) * math.pow(xs[0], x)
    else:
        ans = math.floor(xs[1]) * math.pow(xs[0], x)
        return (ans, ans**2)

# Test the functions
print(poly([1, 2])) # f(x) = 1 + 2x
print(find_zero([1, 2])) # return (x-1)
```