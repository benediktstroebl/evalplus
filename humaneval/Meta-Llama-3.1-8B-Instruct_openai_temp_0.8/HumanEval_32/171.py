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
    Finds a zero of a polynomial given its coefficients.
    xs are coefficients of a polynomial. The returned zero is found using
    the largest non-zero coefficient as a root of the polynomial formed by
    all other coefficients.

    :param xs: list of coefficients of the polynomial
    :return: x such that poly(x) = 0
    """
    if len(xs) % 2!= 0 or not any(coeff!= 0 for coeff in xs):
        raise ValueError("Polynomial coefficients must be a list with an even number of elements and at least one non-zero coefficient")
    
    # Create a new polynomial with the largest non-zero coefficient as coefficient 1
    new_xs = [coeff / xs[np.argmax([c for c in xs if c!= 0])] for coeff in xs if coeff!= 0]
    # Remove the largest coefficient (now 1) to make the polynomial monic
    new_xs.pop(np.argmax([c for c in xs if c!= 0]))
    
    # Find the root of the new polynomial, which is a root of the original polynomial
    return -np.poly1d(new_xs).r  # The `r` attribute returns the root of a monic polynomial

# Test cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses `numpy` to create a polynomial and find its root. The `np.argmax` function is used to find the index of the largest coefficient in the polynomial. This index is used to remove the largest coefficient from the polynomial to make it monic. The `np.poly1d.r` attribute is then used to find the root of the monic polynomial, which is a root of the original polynomial.

The test cases at the end of the script demonstrate the usage of the `find_zero` function.