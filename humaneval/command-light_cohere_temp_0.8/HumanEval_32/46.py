```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    )

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    and takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    """
    return x

xs = [1, 2, -5]
poly = find_zero(xs)
print("The value of polynomial x^2 + 3x + 4 with coefficients is:", poly)  # 2.0localhost

print("The roots of the polynomial x^2 + 3x + 4 are:", poly)  # 2.0localhost
```