```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2!= 0 or xs[-1] == 0:
        raise ValueError("List xs must have even number of coefficients and the largest coefficient must be non-zero")

    n = len(xs)
    x = -xs[1] / (xs[0] * 2)
    return x

# Test cases
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

However, note that the solution relies on an approximation to find the root, and there's no guarantee that the root is exact. Also, this function will only find a single root, and there's no guarantee that this root is the one closest to the root that the function was approximating.

This approximation is based on the formula `x = -b / (2a)`, which is a first-order Taylor expansion of the function `f(x) = ax^2 + bx + c` around the point where the derivative is zero.

If you need a more accurate solution, you might want to look into numerical methods for finding roots, such as the Newton-Raphson method. 

Here's a version of the `find_zero` function that uses the Newton-Raphson method:

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_derivative(xs: list, x: float):
    """
    Evaluates derivative of polynomial with coefficients xs at point x.
    """
    return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2!= 0 or xs[-1] == 0:
        raise ValueError("List xs must have even number of coefficients and the largest coefficient must be non-zero")

    n = len(xs)
    x = 1.0  # initial guess
    for _ in range(100):  # maximum number of iterations
        x_new = x -