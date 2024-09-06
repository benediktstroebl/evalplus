```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and returns largest non zero coefficient in xs as it guarantees
    a solution.

xs=[1,2]
xs = [x**3 - 2*x - 6, x**2 + x + 1]
poly(xs, x) # x**3 - 2*x - 6 + x**2 + x + 1 = 0
find_zero(xs)
print(f"x": end="")
print(find_zero(xs)[0])
```