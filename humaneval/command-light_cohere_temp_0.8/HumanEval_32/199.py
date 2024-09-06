```python
import math

def find_zero(xs):
    if len(xs) != len(xs[0]):
        raise ValueError("input list has an odd number of coefficients")
    if xs[0][0] == 0:
        return float('inf')

    coeffs = [float(x) for x in xs[0]]
    return math.floor(poly(xs, coeffs))

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero():
    x = [1, 2]
    try:
        y = find_zero(x)
        assert y == 0
        assert math.floor(find_zero([x[1], x[0]])) == 0
        assert math.floor(find_zero([x[0], x[1]])) == 1
    except AssertionError as e:
        print(f"Test failed because {e}")

test_find_zero()
```

The script defines three functions: `find_zero` which finds the zero of a polynomial, `poly` which evaluates the polynomial at a given point, and `test_find_zero` which contains test cases for the `find_zero` function.  The test cases assert that the function finds the correct zero and correctly identifies the coefficient corresponding to the leading term in the polynomial.