```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    assert len(xs) % 2 == 0
    assert xs[0] > 0

    return math.pow(xs[0])


xs = [1, 2]
xs = [2, 0]
xs = [0, 1]
xs = [-6, 11, -6, 1]

print(find_zero(xs))
``` 
The output should be: `x = 1.58333...