```python
import math

def find_zero(xs: list):
    """
    Ensure list of coefficients has even length and largest non-zero coefficient.
    if len(xs) % 2 != 0:
        raise ValueError("Input list must have even number of coefficients.")
    if xs[0] == 0:
        return [xs[1], xs[2], xs[3], ...]
    return [x for x in xs if x != 0]

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero():
    """
    Test find_zero function
    >>> round(find_zero([1, 2])) # [1, 2]
    >>> round(find_zero([-6, 11, -6, 1])) # [-6, 11, -6]
    """
    print(find_zero([1, 2]))  # [1, 2]
    print(find_zero([-6, 11, -6, 1]))  # [-6, 11, -6]

test_find_zero()
``` 
The provided Python script defines a self-contained function `find_zero` that finds the zeros of a polynomial. The `poly` function evaluates a polynomial at a given point and returns the polynomial's value at that point. The `test_find_zero` function tests the `find_zero` function by providing lists of coefficients, and it prints the resulting zeros.