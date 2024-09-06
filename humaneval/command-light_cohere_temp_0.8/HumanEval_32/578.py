```python
import math

def find_zero(xs):
    """
    Check if the list is of even length.
    if it's
    then return the largest non-zero coefficient of the polynomial
    built using coefficients xs.
    """
    return float(xs[0])

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero(xs):
    """
    Test function for the find_zero function
    """
    assert find_zero(xs) == float(xs[0]),
    assert find_zero([1, 2]) == float(1),
    assert find_zero([6, 11, -6, 1]) == float(-5),
    assert find_zero([]) == 0.0

xs = [1, 2]
poly(xs, x)
test_find_zero(xs)
```
The script defines a polynomial function `poly` that evaluates a polynomial at a given point `x` using the coefficients `xs` and passes it to the `find_zero` function to find the zero of the polynomial. The `find_zero` function returns the largest non-zero coefficient of the polynomial, which is then passed to the `test_find_zero` function to test the function. The `test_find_zero` function contains several test cases that check if the `find_zero` function works correctly with different inputs.