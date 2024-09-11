```python
import numpy as np
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial defined by coefficients xs.
    
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    
    Parameters:
    xs (list): coefficients of the polynomial.
    
    Returns:
    float: a zero point of the polynomial.
    """
    if len(xs) % 2!= 0 or not any(coeff!= 0 for coeff in xs):
        raise ValueError("List xs must have even number of coefficients and a largest non-zero coefficient.")
    
    n = len(xs) // 2  # number of roots
    roots = np.roots(xs)
    # select a root with largest magnitude
    return max(roots, key=lambda x:abs(x))

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x, expected: -0.5
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3, expected: 1.0
```

This script uses the `numpy` library to find the roots of the polynomial. The `np.roots` function returns all roots, so we select the one with the largest magnitude. 

We also added some error checking to ensure that `xs` has an even number of coefficients and a largest non-zero coefficient. This guarantee a solution as the problem statement claims.