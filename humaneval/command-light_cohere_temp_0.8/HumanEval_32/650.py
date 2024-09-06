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
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    """
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have even number of coefficients")
    return math.floor(find_zero(xs))

test_poly = [1, 2,3]
test_find_zero = [1, -3]

print("poly result:", poly(test_poly, 1))
print("find_zero result:", find_zero(test_find_zero))
``` 
This script defines a function `poly` that computes the polynomial with given coefficients at a given point `x`. The function `find_zero` finds the zeros of the polynomial `poly` at `x`. The script then prints the results of these functions for the given test inputs.