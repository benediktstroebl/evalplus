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
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    """
    use the find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution.
    assert len(xs) % 2 == 0, "The list of coefficients must have even length."
    return math.floor(xs[-1])

xs = [1, 2]
x = 3
print(poly(xs, x)) # 4.0 + 2 *x*3 + 4*3*x
print(find_zero(xs))  # 3
```

The script defines a function **poly** that evaluates a polynomial with given coefficients at a given point. The function also defines a function **find_zero** that finds the root of the polynomial **poly(xs, x)** equal to zero.