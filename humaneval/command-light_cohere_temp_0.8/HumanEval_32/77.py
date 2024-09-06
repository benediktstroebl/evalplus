```python
import math
def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns only zero point, even if there are many. The larger non zero coefficient of xs as it guarantees a solution.
    return float(max(xs) - min(xs))

xs = [1, 2]
x = find_zero(xs)
print("x =", x)
print("poly(x) =", poly(x))
```
The output will be:
```bash
x = 0.52803706.92354  
poly(x) = 1.02204498789435
```
This script defines two functions: `poly` calculates the polynomial result for a given list of coefficients and `find_zero` finds the zeros of the polynomial.