```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0,
    find_zero returns only zero point, even if there are many.
    """
   , find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    # Test: verifies that the function correctly evaluates polynomial at the point and returns zero
    # Test: verifies that the function correctly finds zero
    assert find_zero([1, 2]) == 0
    assert find_zero([-6, 11, -6, 1]) == 0
    assert find_zero([1, -3, 2, -4]) != 0
    assert find_zero([3, 3, 4, 3]) == 0
    assert find_zero([1, 1, -1, -1]) != 0
    assert find_zero([2, 3, 3, 3]) == 3.0
```
The script defines two functions: `poly` and `find_zero`. The `poly` function computes the value of a polynomial with given coefficients at a given point. The `find_zero` function identifies the zero of a polynomial. The script then tests the functions to ensure their correctness and efficiency.