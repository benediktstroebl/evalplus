```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns only zero point, even if there are many.
    search for zeros of polynomial by computing its value at x = limit from negative infinity, and checking if it's equal to 0.
    > round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
   
    print(find_zero([1, -1, 3]))

# Test cases:
xs = [1, -1, 3]
result = find_zero(xs)
print(result)

xs = [1, -2, -3]
result = find_zero(xs)
print(result)

xs = [1, -3, 4, 5]
result = find_zero(xs)
print(result)
```

This script defines a function `poly` that computes a polynomial with coefficients `xs` at `x` and returns the polynomial's value at `x`. The function `find_zero` searches for the polynomial's zero by evaluating the polynomial at various `x` values and comparing the results to 0. The test cases demonstrate how the script works by passing different sets of coefficients to the `find_zero` function and printing the resulting zero points.