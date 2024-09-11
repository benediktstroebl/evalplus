```markdown
### Polynomial Zero Finder

This script defines a function `find_zero` to find a zero of a polynomial given its coefficients.

```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n

    Args:
        xs (list): coefficients of the polynomial
        x (float): point at which to evaluate the polynomial

    Returns:
        float: value of the polynomial at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial given its coefficients.

    Args:
        xs (list): coefficients of the polynomial

    Returns:
        float: a zero of the polynomial

    Raises:
        ValueError: if the number of coefficients is odd
    """
    if len(xs) % 2!= 0:
        raise ValueError("Number of coefficients must be even")
    if xs[-1] == 0:
        raise ValueError("Largest non-zero coefficient must be non-zero")

    # Use numpy's roots function to find all zeros
    zeros = np.roots(xs)

    # Check if there are any real zeros
    real_zeros = [z.real for z in zeros if z.imag == 0]

    # Return the first real zero
    return real_zeros[0]

# Example use cases
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

This script uses the `numpy` library to find all zeros of the polynomial using the `roots` function. It then returns the first real zero.

Note that this script assumes that the largest non-zero coefficient is in the last position of the `xs` list. If this is not the case, you will need to modify the script to find the largest non-zero coefficient and swap it with the last coefficient before calling `find_zero`.