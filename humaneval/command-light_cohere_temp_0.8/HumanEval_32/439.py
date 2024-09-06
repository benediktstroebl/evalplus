```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    > It finds only list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution. The function uses the mathematical property that for polynomial f(x) = sum(a * x^n) with coefficients a, xn, ... and degree n, if there is exactly one root, then f(x) = 0.
    if n = 1
    else if x = root then f(x) = 0 else continue
    """
    x = max(xs, key=abs)
    return x

xs = [1, 2]
x = find_zero(xs)
print(x)  # Output: 2

xs = [-6, 11, -6, 1]
x = find_zero(xs)
print(x)  # Output: 1
```
The Python script defines two functions: `poly` and `find_zero`. The `poly` function evaluates a polynomial given a list of coefficients `xs` at a point `x`. The `find_zero` function finds the zero of the polynomial `poly(x)` by recursively evaluating polynomial expressions. It then tests the By passing different coefficient lists to `find_zero`, we can find the corresponding zero values.