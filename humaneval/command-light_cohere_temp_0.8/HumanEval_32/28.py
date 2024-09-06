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
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    >> Use, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

poly([1, 2]) # [1, 2]
xs = [1, -6, 11, -6, 1]
xs = [1, -6, 11, -6, 1, -2]
xs = [1, 2, -3, -4, -3, -4, -5]
xs = [-6, 11, -6, 1, -2]
xs = [-6, 11, -6, 1, -2, -3, -4]
xs = [1, -3, -4, -3, -4, -5, -6]
xs = [1, -6, -6, -3, -4, -6, -7]
xs = [-6, 11, -6, -3, -4, -7, -8]
xs = [1, 2, -3, -4, -5, -3, -6]

print(find_zero(xs))
``` 
Output: 

-1.