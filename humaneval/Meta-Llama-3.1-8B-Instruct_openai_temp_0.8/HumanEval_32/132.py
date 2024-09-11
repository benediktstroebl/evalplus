```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs[::-1])])


def poly_np(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x using numpy.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * np.power(x, i) for i, coeff in enumerate(xs[::-1])])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Ensure the list has an even number of elements (including the leading coefficient)
    assert len(xs) % 2 == 0, "Polynomial must have an even number of coefficients"
    
    # Sort coefficients in descending order
    xs = sorted(xs, reverse=True)
    
    # Find the largest non-zero coefficient
    largest_coeff_idx = next((i for i, x in enumerate(xs) if x!= 0), None)
    
    # Solve the equation using the quadratic formula
    a = -xs[largest_coeff_idx]
    b = xs[largest_coeff_idx + 1]
    c = -xs[largest_coeff_idx + 2]
    
    if a == 0:
        if b == 0:
            return "Infinite number of solutions"
        else:
            return -c / b
    else:
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            return "No real solutions"
        elif discriminant == 0:
            return -b / (2*a)
        else:
            return (-b + np.sqrt(discriminant)) / (2*a), (-b - np.sqrt(discriminant)) / (2*a)


import unittest

class TestPolyAndFindZero(unittest.TestCase):

    def test_poly_with_symbolic_vars(self):
        #Testing with symbolic variables
        self.assertAlmostEqual(poly([1, 2], 0), 1)
        self.assertAlmostEqual(poly([1, 2], 1), 3)
        self.assertAlmostEqual(poly([1, 2], -1), -1)
        
    def test_poly_np_with_symbolic_vars(self):
        #Testing with numpy
        self.assertAlmostEqual(poly_np([1, 2], 0), 1)
        self.assertAlmostEqual(poly_np([1, 2], 1), 3)
        self.assertAlmostEqual(poly_np([1, 2], -1), -1)
        
    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5)
