### Find Zero of a Polynomial Script

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Separate coefficients into two lists
    # one for non-zero terms and one for zero terms
    non_zero = []
    zero = []
    for i, coeff in enumerate(xs):
        if coeff!= 0:
            non_zero.append(coeff)
        else:
            zero.append(coeff)

    # Construct polynomial from non-zero terms
    poly_str = ""
    for i, coeff in enumerate(non_zero):
        if i == 0:
            poly_str += f"{coeff}"
        elif i == 1:
            poly_str += f" + {coeff}x"
        else:
            poly_str += f" + {coeff}x^{i}"
    
    # Check if polynomial is linear
    if len(non_zero) == 2:
        # Find x such that poly(x) = 0
        x = -non_zero[1] / non_zero[0]
        return round(x, 2)
    
    # If polynomial is not linear, try to factor it
    else:
        try:
            # Try to factor polynomial using numpy
            roots = np.roots(non_zero)
            # Find real root
            real_root = [root.real for root in roots if root.imag == 0][0]
            return round(real_root, 2)
        except ValueError:
            # If polynomial cannot be factored, return None
            return None

# Test the function
print(find_zero([1, 2]))
print(find_zero([-6, 11, -6, 1]))
```

This script first separates coefficients into two lists, one for non-zero terms and one for zero terms. It then constructs a polynomial string from the non-zero terms. If the polynomial is linear, it finds the root directly. If the polynomial is not linear, it tries to factor it using numpy's roots function. If the polynomial cannot be factored, it returns None.