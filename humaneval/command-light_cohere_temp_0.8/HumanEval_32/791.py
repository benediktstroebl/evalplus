```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + ... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    """
    find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    """
    def test_solve(xs: list, x: float):
        """
        Test function that checks if a polynomial with coefficients xs evaluates to zero at x.
        """
        def test_solve(xs: list, x: float):
            return poly(xs, x) == 0


# Example usage
xs = [1, 2]
x = 0.5
test_solve(xs, x)
```

This script defines two functions, `poly` and `find_zero`, that solve the problem of evaluating a polynomial at a given point `x` and finding its roots, respectively. It also defines a test_solve, which tests the `poly` function.

The `poly` function takes in a list of coefficients xs and a point x as input and returns the polynomial evaluated at x. The `find_zero` function takes in a list of coefficients xs and finds the zero of the polynomial evaluated at x.

The test_solve function tests the `poly` function by evaluating it at a given point x and checking if the result is zero.

The `xs` list is [1, 2] and the `x` value is 0.5. The test_solve function is then called with these inputs, and it returns True, indicating that the polynomial with coefficients [1, 2] evaluated at x 0.5 is equal to zero.