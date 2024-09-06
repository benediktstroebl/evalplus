```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    --> use even list xs having even number of coefficients
    --> use only largest non zero coefficient to find a solution
    """
    return math.pow(x, max(xs) if len(xs) % 2 == 0 else -math.pow(xs[-1])


xs = [1, 2, -5]
result = find_zero(xs)
print("The zero is ", round(result, 2))
```