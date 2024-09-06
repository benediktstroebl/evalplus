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
    find_zero find x that makes the polynomial equal to zero
    find_zero returns x, even if there are many solutions"""
    x = -math.polygcd(xs[0], xs[1])[0]
    return x


xs = [1, 2]
xs2 = [6, 11, -6, 1]
print(poly(xs, 2.0))
print(find_zero(xs))
print(find_zero(xs2))
```
The code is well-formatted and follows the standard format for Python code. It defines two functions: `poly` and `find_zero`. `poly` calculates the value of a polynomial at a given point `x` by summing the product of the polynomial's coefficients and the power of `x` to each coefficient. `find_zero` finds the don't care about the number of solutions, as long as the polynomial is zero. The code also prints the results of the function calls to the console.