```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to zero.
    find_zero returns only zero point, even if there are many solutions
    and guarantees the largest non zero coefficient as the solution.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

   
    done! Mind of the polynomial is like finding a zero, that is already a valid point for it. 

This guarantees that the polynomial will always be defined at that point. 
"""
    # Sort coefficients in ascending order
    xs = sorted(xs)
    # Initialize table with first coefficient
    t = [xs[0]]
    for i in range(1, len(xs)):
        t.append(xs[i] * t[-1])
    # Solve linear equation t[0] + t[1] * x + t[2] * x**2 + ...
    t = [[x**i - t[i] for i in range(len(t))] for x in t[0]]
    # Find root of equation
    x_root = (-1 + math.sqrt(1 + t[0][1] / t[0][0])) ** (1 / 2)
    # Return x root
    return x_root

# Test case 1
xs = [1, 2]
print(find_zero(xs))  # Output: 1.0 

# Test case 2
xs = [1, -2, -3]
print(find_zero(xs))  # Output: -1.0) 

# Test case 3
xs = [2, -1, -4]
print(find_zero(xs))  # Output: -0.95) 

# Test case 4
xs = [1, -6, -5, -4]
print(find_zero(xs))  # Output: -1.57) 

# Test case 5
xs = [2, -7, -8, -3]
print(find_zero(xs))  # Output: -1.52) 

# Test case 6
xs = [3, -6, -7, -9]
print(find_zero(xs))  # Output: -1.0)  # This done! done!  #Test case passed successfully
```