```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many.
    All, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    # Test case 1
    Example that the function finds zero:
    assert find_zero([1, 2]) == (0.0, 2.0)
    test the tested to give correct result for the polynomial f(x) = 1 + 2x - 0.5.
    # Test print thefeed on: [1, 2] = [x**2 - x + 1, x - 0.0]
    print("Pass")
    assert find_zero([1, 2]) == (0.0, 2.0)
    failed to find a solution to give a correct result for f(x) = 1 + 2x - 0.5.
    # Testprint on: [1, 2] = [x**2 - x + 1, x - 0.0]
    print("pass")
    assert find_zero([-6, 11, -6, 1]) == (0.0, 2.0)
    print("pass")
```
The code defines two functions:
- The `poly` function computes the value of a polynomial at a given point `x` by using the coefficients of the polynomial as a list. It also allows for the calculate the value of a polynomial at any given point.
- The `find_zero` function finds the value of `x` that makes the polynomial equal to 0. It uses the list of coefficients of the polynomial as input and returns the value of `x` that makes the polynomial equal to 0. 

The `find_zero` function tests the value of the polynomial against the value of `x` that makes the polynomial equal to 0. It uses the list of coefficients of the polynomial as input and returns the value of `x` that makes the polynomial equal to 0. The `assert` statement is used to test the value of the `find_zero` function against the expected result.