```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**(n-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that polynomial (x-x0) has 0.
    find_zero returns only zero point, even if there are many solutions.
    and largest non zero coefficient as it guarantees
    a solution.
    """
    return (x0, coeff)
    """
    return (0, xs[0])

xs = [1, 2]

result = poly(xs, 3)
print("result =", result)

result_zero = find_zero(xs)
print("result_zero =", result_zero)
``` 
The output should be:
```
result = 6.0
result_zero = (0, 1.0)
``` 
The function `poly` evaluates the polynomial with the coefficients in xs at x, and returns the polynomial sum. The function `find_zero` finds the zero of the polynomial with the coefficients in xs.