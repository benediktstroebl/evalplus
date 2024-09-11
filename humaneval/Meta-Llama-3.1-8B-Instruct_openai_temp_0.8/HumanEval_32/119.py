```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def poly_np(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x (using numpy).
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    xs = np.poly1d(xs)
    return xs(x)

def find_zero_np(xs: list):
    """
    Find x such that poly(x) = 0 (using numpy)
    returns all roots of the polynomial (including complex ones)
    """
    if len(xs) % 2!= 0:
        raise ValueError("list must have even number of coefficients")
    
    xs = np.poly1d(xs)
    return np.roots(xs)

def find_zero_simple(xs: list):
    """
    find x such that poly(x) = 0 (using simple methods for quadratics and cubics)
    returns only real roots of the polynomial
    """
    if len(xs) % 2!= 0:
        raise ValueError("list must have even number of coefficients")
    
    # try to identify a quadratic equation
    if len(xs) == 4:
        a, b, c = xs[3], xs[2], xs[1]
        d = -b / (2 * a)
        discriminant = b**2 - 4 * a * c
        if discriminant >= 0:
            root1 = d + math.sqrt(discriminant) / (2 * a)
            root2 = d - math.sqrt(discriminant) / (2 * a)
            if root1 == root2:
                return root1
            else:
                return root1, root2
        else:
            real_part = d
            imaginary_part = math.sqrt(-discriminant) / (2 * a)
            return complex(real_part, imaginary_part)
    
    # try to identify a cubic equation
    elif len(xs) == 6:
        a, b, c, d = xs[5], xs[4], xs[3], xs[2]
        p = (3 * a * c - b**2) / (9 * a**2)
        q = (9 * a * b * c - 27 * a**2 * d - 2 * b**3) / (54 * a**3)
        discriminant = q**2 + 4 * p**3
        base = 2 * p
        root1 = (-q + math.sqrt(discriminant))**(1./3) - base**(1./3)
        root2 = (-q - math.sqrt(discriminant))**(1./3) - base**(1./3)
        root3 = 1/ (root1 + root2)
        return root1, root2, root3
    
    else:
        return find_zero_np(xs)

# Test cases
print(round(find_zero_simple([1, 2]), 2)) # f(x) = 1 + 2x
print(round(find_zero_simple([-6, 11, -6, 1]), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^