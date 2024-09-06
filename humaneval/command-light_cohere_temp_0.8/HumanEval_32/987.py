```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x ** 2 + ... xs[n] * x ** (n - 1))

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial poly(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    """
    root of the above polynomial: 1 + 2x -0.5
    Note that coefficients should be [real coefficient, x, imaginary coefficient]
    """
    return 0 + math.sqrt(1 + xs[0] * x - xs[1] * x ** 2 - ... - xs[-1] * x ** (n - 1))

# Test the function
test_poly = [1, 2, -0.5, -5, 1]
test_zero = [1, -2, 3, 4]

result = poly(test_poly, 2)
result = find_zero(test_zero)

print(result)
``` 
This Python script defines a function `poly` that computes a polynomial with given coefficients at a specified point `x`. It also defines a function `find_zero` that finds the `x`-coordinate that makes the polynomial equal to zero.

The script then tests the `poly` and `find_zero` functions with sample inputs and prints the results.