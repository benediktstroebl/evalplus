```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, len(xs) - i - 1) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds x such that poly(x) = 0.
    xs are coefficients of a polynomial.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if number of coefficients is even
    if len(xs) % 2!= 0:
        raise ValueError("Number of coefficients must be even")

    # Check if largest coefficient is non-zero
    if xs[-1] == 0:
        raise ValueError("Largest coefficient must be non-zero")

    # Convert coefficients to numpy array
    xs = np.array(xs)

    # Use numpy.roots to find all roots
    roots = np.roots(xs)

    # Return the first root (we know there is at least one)
    return roots[0]
```

Note that we're using `numpy.roots` to find all roots of the polynomial, and then just returning the first one. This is because `numpy.roots` can find all roots of a polynomial, but your original specification only required you to find one. If you want to find all roots, you can modify the function to return `roots`.

Also note that we're checking if the number of coefficients is even and if the largest coefficient is non-zero, as per your original specification. If either of these conditions is not met, we raise a `ValueError`.