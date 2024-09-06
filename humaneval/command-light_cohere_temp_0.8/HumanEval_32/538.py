```python
import math
def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero returns only zero point, even if there are many.
    However, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    """
    def evaluate_poly(xs: list, x:float):
        """
        xs are coefficients of a polynomial
        evaluate polynomial with coefficients xs at point x
        return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
        """
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients must have even length")
    m = max(xs, key=abs)
    return evaluate_poly(xs[:-len(xs) // 2], x=x / m)
try:
    print(find_zero([1, 2, 3]))
except ValueError as e:
    print(e)
```