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
    find_zero returns only zero point, even if there are many
    and it guarantees a solution because it takes list xs having even number of coefficients and largest non-zero coefficient as it ensures
    a solution.
 ```
# Test
xs = [1, 2]
xs = [1,2,5,-6]
xs = [-6, 11, -6, 1]
print(find_zero(xs))
```