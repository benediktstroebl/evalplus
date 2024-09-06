```python
import math
def evaluate_polynomial(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coefficient * math.pow(x, i) for i, coefficient in enumerate(xs)])

def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to zero
    find_zero returns only zero point, even if there are many.
    and finds_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.

def test_find_zero():
    xs = [1, 2, -3, -4]
    assert evaluate_polynomial(xs, x=0) == 0
    assert evaluate_polynomial(xs, x=1) != 0
    assert evaluate_polynomial(xs, x=2) != 0
    assert evaluate_polynomial(xs, x=3) != 0
    assert evaluate_polynomial(xs, x=4) != 0
    assert find_zero(xs) == 0

test_find_zero()
```

In this script, we have a function evaluate_polynomial that calculates the value of a given polynomial at a given point x. The function also has a test_find_zero function, which tests the find_zero function with various input arguments to ensure it returns the correct result. 

Note that the test_find_zero function calls the evaluate_polynomial function with the appropriate arguments to test the correctness of the functions.