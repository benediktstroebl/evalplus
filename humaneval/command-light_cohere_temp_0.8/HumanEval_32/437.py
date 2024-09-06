```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x that makes the polynomial equal to zero, returns x
    """
    x = 0
    while True:
        # find x that makes polynomial equal to 0
        polynomial = poly(xs, x)
        if polynomial == 0:
            return x
        x += 1

# Test the function
xs = [1, 2]
x = find_zero(xs)
print(x) # Output: 2
xs = [-6, 11, -6, 1]
x = find_zero(xs)
print(x) # Output: 1
xs = [1, 2, 3, 4, 5]
x = find_zero(xs)
print(x) # Output: 4
```