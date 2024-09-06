```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial(x) = 0.
    find_zero returns only zero point, even if there are many roots.
    """
    return x[0]
    """
    if len(xs) == 1:
        return float('inf')
    elif len(xs) % 2 != 0:
        return float('inf')
    else:
        # find the index of the largest coefficient
        i = xs.index(xs[0] + 1
        while i < len(xs) - 1 and xs[i] == xs[i + 1]:
            i += 1
        return xs[i]

# Test the function
xs = [1, 2]
x = float('inf')
ans = find_zero(xs)
print('x =', end='')
print(x, end='')
print('=' , ans)

xs = [1, -6, 11, -6, 1]
x = float('inf')
ans = find_zero(xs)
print('x =', end='')
print(x, end='')
print('=' , ans)

xs = [-6, 11, -6, 1]
x = float('inf')
ans = find_zero(xs)
print('x =', end='')
print(x, end='')
print('=' , ans)

xs = [1, -1]
x = -1
ans = find_zero(xs)
print('x =', end='')
print(x, end='')
print('=' , ans)
```
The code defines a function `poly` that computes the polynomial with coefficients in `xs` at a given point `x`. It then defines the `find_zero` function that finds the value of `x` that makes the polynomial equal to zero. Finally, it tests the `find_zero` with different sets of coefficients and prints the result.