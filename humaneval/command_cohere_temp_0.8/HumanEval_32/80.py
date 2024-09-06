Here's a Python script that includes a function to solve the problem of finding a zero point of a polynomial:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check for polynomial with even number of coefficients
    if len(xs) % 2 == 0:
        x = 0
        current_val = xs[0]
        for i in range(1, len(xs)):
            current_val = current_val * (x**2) + xs[i] * x + poly(xs[:i]+xs[i+1:], x)
            if current_val == 0:
                return x
            x += 1
    else:
        print("Given list xs does not have even number of coefficients.")
    return None
```

This script includes a function `find_zero` that finds the single zero point of a polynomial with even coefficients, handling cases where there are multiple zero points and ensuring the result is a single solution.

The `poly` function evaluates the polynomial at a given point `x`.