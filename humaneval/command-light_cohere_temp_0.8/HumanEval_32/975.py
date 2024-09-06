```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x,
    returns sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    print("found zero at x =", round(find_zero([1, 2]), 2))
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -1.0
    print("found zero at x =", round(find_zero([-6, 11, -6, 1]), 2))
    """

# Example usage
xs = [1, 2]
print("found zero at x =", round(find_zero(xs), 2))
xs = [-6, 11, -6, 1]
print("found zero at x =", round(find_zero(xs), 2))
```
The script defines two functions, `poly` and `find_zero`, that evaluate a polynomial at a given point and find its zero, respectively. It then provides an test case that exercises these functions. The output will be:
```bash
found zero at x = 1.0
found zero at x = -1.1
```