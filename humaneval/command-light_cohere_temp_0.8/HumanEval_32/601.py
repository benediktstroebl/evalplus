```python
import math

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero returns only zero point, even if there are many.
    However, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    return round(xs[0] / xs[1] / xs[2] / ... / xs[-1], 2)

def test_find_zero():
    """
    test_find_zero checks if the returned x value is an integer and evaluates to zero.
    test_find_zero returns True if correct
    """
    assert find_zero([1, 2]) == 0
    assert find_zero([-6, 11, -6, 1]) == 0
    assert find_zero([1, -1, -2, -3]) != 0

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

# Driver code
if __name__ == "__main__":
    test_find_zero()
    poly([2, -3, 4], 1)
```

This code defines two functions: `find_zero` and `poly`. The `find_zero` function finds the zero of a polynomial with coefficients given by the list `xs`. The `poly` function evaluates the polynomial at a given point `x`.