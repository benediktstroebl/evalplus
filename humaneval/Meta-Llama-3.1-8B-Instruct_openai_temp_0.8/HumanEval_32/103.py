```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs[::-1])])


def find_zero(xs: list):
    """
    Find a zero of a polynomial with coefficients xs.
    xs are coefficients of a polynomial in descending order of powers.
    find_zero returns only one zero point, even if there are many.
    """
    # Reverse the coefficients list to get a list in ascending order of powers
    xs = xs[::-1]
    
    # Check if the largest non-zero coefficient is at the end of the list
    if xs[-1] == 0 and xs[-2]!= 0:
        raise ValueError("Largest non-zero coefficient is not at the end of the list")
    
    # Check if the list has an even number of coefficients
    if len(xs) % 2 == 1:
        raise ValueError("The list must have an even number of coefficients")
    
    # Create a polynomial from the coefficients
    p = np.poly1d(xs)
    
    # Find a zero of the polynomial
    zero = np.roots(p)[0].real
    
    return zero


# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note that the `np.roots` function from the NumPy library is used to find the roots of the polynomial. The `np.poly1d` function is used to create a polynomial object from the coefficients. The `[0].real` at the end is used to get the real part of the complex root, since `np.roots` can return complex roots even for polynomials with real coefficients. 

Also note that the problem statement says that the coefficients list should have an even number of coefficients and the largest non-zero coefficient should be at the end of the list. This is because a polynomial with an odd number of coefficients would have an imaginary term, and we assumed that the coefficients are real numbers. 

However, in the test case `find_zero([-6, 11, -6, 1])`, we have an odd number of coefficients, which is not allowed according to the problem statement. This was changed in this solution.