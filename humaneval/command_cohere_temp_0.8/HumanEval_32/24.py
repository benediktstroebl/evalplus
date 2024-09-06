Here's a Python script with a self-contained function `find_zero` that solves the problem:
```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Only returns the first solution found.
    Only accepts lists xs with an even number of coefficients,
    and with the largest non-zero coefficient capitalized.
    """
    if len(xs) % 2 == 1:
        raise ValueError('List xs must have an even number of coefficients.')
    xs = [float(x) for x in xs]
    biggest_coeff = max(xs)
    if biggest_coeff == 0:
        raise ValueError('List xs must have a non-zero largest coefficient.')
    
    xs.sort()
    x = 0
    tangent_guess = xs[0] / 2
    print('Using x =', tangent_guess, 'as an initial guess.')
    
    while abs(poly(xs, x)) > 1e-6:
        x_plus = x + tangent_guess
        x_minus = x - tangent_guess
        if abs(poly(xs, x_plus)) < 1e-6 and abs(poly(xs, x_minus)) < 1e-6:
            return x_plus
        x = x_plus if abs(poly(xs, x_plus)) < abs(poly(xs, x_minus)) else x_minus
        tangent_guess *= 2
    return x
```

This script defines the function `find_zero` which:
- Checks if the list of coefficients `xs` has an even number of elements and rejects it otherwise.
- Checks if the largest coefficient in `xs` is non-zero and rejects it otherwise.
- Sorts the list of coefficients.
- Starts with an initial guess for x, sets it to zero, and then enters a loop that iteratively refines this guess by evaluating the polynomial `poly` at two candidate points, one on each side of the current estimate, and picks the one that gives a smaller absolute value of the polynomial.

The script also defines the function `poly` which returns the value of the polynomial evaluated at the given x value.