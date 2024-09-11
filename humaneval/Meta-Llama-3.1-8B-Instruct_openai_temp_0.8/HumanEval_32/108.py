### Polynomial Zero Finder

```python
import math
import numpy as np
from scipy.optimize import root_scalar

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.

    Args:
    - xs: List of coefficients
    - x: Point to evaluate the polynomial at

    Returns:
    - Value of the polynomial at x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Find the zero of a polynomial with given coefficients.

    Args:
    - xs: List of coefficients

    Returns:
    - Zero of the polynomial
    """
    if len(xs) % 2!= 0:
        raise ValueError("List of coefficients must have an even number of elements")

    # Use numerical method to find the root
    def f(x):
        return poly(xs, x)

    result = root_scalar(f, bracket=[-10, 10])  # Set a bracket to find the root
    return result.root
```

### Example Usage

```python
# Example 1: f(x) = 1 + 2x
print(round(find_zero([1, 2]), 2))  # Output: -0.5

# Example 2: (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
print(round(find_zero([-6, 11, -6, 1]), 2))  # Output: 1.0
```

Note that `find_zero` function uses the `root_scalar` function from `scipy.optimize` to numerically find the root of the polynomial. This method is more robust and efficient than trying to factor the polynomial or use a closed-form solution.