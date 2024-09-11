### Evaluating Polynomials and Finding Zeroes
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    result = 0
    for i, coeff in enumerate(xs):
        result += coeff * math.pow(x, i)
    return result

def find_zero(xs: list):
    """
    Find x such that poly(x) = 0.
    Assumes xs are coefficients of a polynomial and have an even number of coefficients.
    Largest non-zero coefficient is used to guarantee a solution.
    Returns only one zero point, even if there are many.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2!= 0:
        raise ValueError("Polynomial coefficients must have an even number of elements")
    
    max_coeff_idx = np.argmax(np.abs(xs[:-1]))
    max_coeff = xs[max_coeff_idx]

    if max_coeff == 0:
        raise ValueError("Leading coefficient cannot be zero")

    x = -xs[-1] / max_coeff
    if math.isclose(poly(xs, x), 0):
        return x
    else:
        # If the found x does not exactly solve the polynomial, 
        # we can try to refine it using Newton's method
        return newton_method(xs, x)


def newton_method(xs: list, x: float, epsilon=1e-6, max_iter=1000):
    """
    Use Newton's method to refine the root found by linear approximation.
    """
    for _ in range(max_iter):
        f_x = poly(xs, x)
        f_prime_x = poly([coeff * i for i, coeff in enumerate(xs)], x)
        
        if math.isclose(f_x, 0):
            return x
        
        x_new = x - f_x / f_prime_x
        
        if math.isclose(x_new, x, abs_tol=epsilon):
            return x_new
        
        x = x_new
    
    raise ValueError("Failed to converge after {} iterations".format(max_iter))
```

This script defines two functions, `poly` and `find_zero`. The `poly` function evaluates a polynomial at a given point. The `find_zero` function finds a root of a polynomial given its coefficients. It first tries to find the root using linear approximation, and then uses Newton's method to refine the root if necessary. The script also includes docstrings to explain the purpose and behavior of each function.