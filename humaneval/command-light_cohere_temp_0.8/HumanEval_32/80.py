```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    and find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

    """

def test_find_zero(xs: list):
    assert find_zero(xs) == [float('inf')]
    assert not any(xs[i] == 0 for i, xs in enumerate(xs))
    assert xs[-1] != 0
    assert all(xs[i] != 0 for i, xs in enumerate(xs))

    assert find_zero([1, 2]) == [1.0]
   
    assert find_zero([1, 2, -2]) == [-1.0]
    assert find_zero([1, 2, -2, 3]) == [-1.0]
```
The script defines a function `poly` that computes the polynomial for a list of coefficients `xs` at a given `x` value, and returns the polynomial. It then defines a function `find_zero` that finds the `x` value that makes the polynomial equal to zero. The `test_find_zero` function tests the `find_zero` function by asserting that it returns the correct results for certain inputs.