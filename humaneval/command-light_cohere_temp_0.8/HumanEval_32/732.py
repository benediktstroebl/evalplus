```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and finds only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    """
    highest power with non zero coefficient is:
    >> coeff_largest = max(xs, key=lambda x: x > 0)
    >> len(xs) == len(xs[xs_largest])
    >> len(xs[xs_largest]) == 1
    >> xs[xs_largest] > 0
    >> xs_largest == 1
    """
    return x

xs = [1, 2]
x = find_zero(xs)
print(x)
```