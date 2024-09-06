```python
import math

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero returns only zero point, even if there are many.
    To find the maximum non zero coefficient to guarantee
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    """
   
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
   
    >>> round(find_zero([0, 0, 0, 1, 4]), 2) # x^4 + x^3 + x^2 + x
    -2.0
    """
   
    """
def poly(xs: list, x:float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

# Example usage:
xs = [1, 2]
x = 1.0

answer = poly(xs, x)
print(answer)
answer = find_zero(xs)
print(answer)
```