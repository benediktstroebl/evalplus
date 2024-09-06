```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes the polynomial equal to 0.
    return [x first non-zero x.
    """
   
        biggest coefficient 
    if xs[0] == 0: return 0
    if xs[1] == 0: return x
    for i in range(2, len(xs)):
        if xs[i] == 0: continue
        temp = x
        x = temp - xs[i] / (xs[i] * temp)
        if x < 0: x = -x
    return x


# Test
test_poly = [1, 2, -3]
test_x = find_zero(test_poly)
if test_x == 0:
    print("Test passed!")
else:
    print("Test failed.")
```
The provided code defines a function `poly` that computes the value of a polynomial based on its coefficients. The `find_zero` function searches for the root of the polynomial. The `test_poly` list contains coefficients for a polynomial, and the `test_x` variable is the result of calling `find_zero` with these coefficients. The script verifies if the root is equal to 0, which indicates the polynomial's value is 0 at that point. If the root is 0, the test passes, otherwise, it fails.