Here is the Python script to solve the problem:
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_new(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x using numpy.
    """
    poly_expr = np.poly1d(xs)
    return poly_expr(x)

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    if len(xs) % 2!= 0 or xs[0] == 0:
        raise ValueError("Invalid input: xs must be a list with an even number of coefficients and non-zero largest coefficient")

    roots = np.roots(np.poly1d(xs))
    
    # return the real root that is closest to the x-axis
    closest_real_root = np.min([root.real for root in roots if np.isreal(root)])
    return closest_real_root

# test cases
print(round(find_zero([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
The script defines two versions of the polynomial evaluation function: `poly` (naive implementation using math.pow) and `poly_new` (efficient implementation using numpy's `poly1d` function). The `find_zero` function uses numpy's `roots` function to find the roots of the polynomial.

Note that the `find_zero` function returns the real root that is closest to the x-axis. If there are multiple such roots, it returns the one with the smallest imaginary part.