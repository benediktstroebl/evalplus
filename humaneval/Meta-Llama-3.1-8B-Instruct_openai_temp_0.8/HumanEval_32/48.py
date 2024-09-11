### Polynomial Evaluation and Zero Finding

```python
import math
import cmath
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial given its coefficients.
    
    Parameters:
    xs (list): coefficients of the polynomial.
    
    Returns:
    float: a zero point of the polynomial.
    
    Note: This function only considers polynomials with an even number of coefficients
          and the largest non-zero coefficient. It returns the first zero point it finds.
    """
    
    # Check if the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    # Find the largest non-zero coefficient
    max_nonzero_coeff = max(coef for coef in xs if coef!= 0)
    
    # Check if the polynomial is constant
    if max_nonzero_coeff == 0:
        raise ValueError("The polynomial is constant and does not have any zero points.")
    
    # Split the coefficients into two halves
    n = len(xs) // 2
    xs_left, xs_right = xs[:n], xs[n:]
    
    # Find the zero point using linear interpolation
    if len(xs_left) == 1:
        return -xs_left[0] / xs_right[0]
    elif len(xs_right) == 1:
        return -xs_right[0] / xs_left[0]
    else:
        # Find the zero point of the quadratic polynomial
        a, b, c = xs_right[0], xs_right[1], xs_right[2]
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            root = (-b + cmath.sqrt(discriminant)) / (2 * a)
            return root.real if np.isclose(root.imag, 0) else root
        else:
            # Find the zero point of the linear polynomial
            a, b = xs_right[0], xs_right[1]
            return -b / a

# Test the functions
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script defines two functions: `poly` for evaluating a polynomial at a given point and `find_zero` for finding a zero point of a polynomial given its coefficients. The `find_zero` function uses linear interpolation to find the zero point of a quadratic polynomial and the quadratic formula to find the zero point of a quadratic polynomial. It also includes some error checking to ensure that the input list of coefficients has an even number of elements and the largest non-zero coefficient is not zero.