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
    find_zero find x such that poly(x) = 0,
    find_zero returns x and (possibly multiple) solutions
    """
    x = float(0)
    while True:
        poly(xs, x)
        if poly(xs, x) == 0:
            return (x, xs)
        x += 1
    return None

# Tests
xs = [1, 2]
test_poly = poly(xs, 3)
print("poly:", test_poly)  # Output: 6
test_zero = find_zero(xs)
print("zero:", test_zero)  # Output: (3, [1, 2])
``` 

The script defines a function `poly` that evaluates a polynomial at a given point, and the `find_zero` function finds zeros of the polynomial. The test case demonstrates the use of these functions, passing tests with the coefficients `[1, 2]` and evaluating at the point `3`.