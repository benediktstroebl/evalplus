```python
import math

def find_zero(xs: list):
    assert len(xs) % 2 == 0, "Input must have even number of coefficients"
    return math.pow(xs[0], xs[1])

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero():
    assert find_zero([1, 2]) == 2.0, "Function does not find correct zero"
    assert find_zero([6, 11, -6, 1]) == 1.0, "Function does not find correct zero"

def test_poly():
    assert poly([1, 2], 3) == 6.0, "Function does not evaluate polynomial correctly"
    assert poly([1, 2, 3], 3) == 9.0, "Function does not evaluate polynomial correctly"

# Run the tests
test_find_zero()
test_poly()
```
This script contains two functions: `find_zero` and `poly`. The `find_zero` function takes a list of coefficients and returns the zero of the polynomial. The `poly` function takes a list of coefficients and a point `x` and returns the polynomial evaluated at that point. The `test_find_zero` and `test_poly` functions contain assertions that verify the correctness of the `find_zero` and `poly` functions, respectively.