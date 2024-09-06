```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    Find x-value where polynomial equals zero.
    xs are coefficients of a polynomial.
    find_zero returns only zero point, even if there are many roots.
    and guarantees a maximum possible zero point among all coefficients.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

def test_find_zero():
    """
    Test find_zero function
    """
    assert find_zero([1, 2]) == (-0.5)
   
    assert find_zero([-6, 11, -6, 1]) == (x - 1) * (x - 2) * (x - 3)

# Driver code
if __name__ == "__main__":
    test_find_zero()

```
The code defines three functions: `poly`, `find_zero`, and `test_find_zero`. The `poly` function computes the value of a polynomial at a given point `x`. The `find_zero` function determines the value of `x` that makes the polynomial equal to zero. The `test_find_zero` function contains a few tests to validate the `find_zero` function. 

The `test_find_zero` function then executes these functions to test them.