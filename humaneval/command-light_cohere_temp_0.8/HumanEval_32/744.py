```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only x, even if there are many solutions.
    find_zero returns only list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    """
    return round(x, 2)

xs = [1, 2]
x = round(find_zero(xs), 2)
print(f'The zero of the polynomial is: {x}')
```