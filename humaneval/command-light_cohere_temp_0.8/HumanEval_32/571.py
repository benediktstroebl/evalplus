```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *n *x of polynomial)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many.
    @test: test_poly(xs) is f(x) = xs[0] + xs[1] * x + xs[1] * x^2 + ... xs[n] * x^n
        """
    test_poly = xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    return round(find_zero(test_poly), 2)
```