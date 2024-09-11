```python
import math
import numpy as np
from scipy.optimize import fsolve

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Ensure the length of coefficients is even
    if len(xs) % 2!= 0:
        raise ValueError("Coefficients list must have an even number of elements")

    # Define a function to find the root of
    def func(x):
        return poly(xs, x)

    return fsolve(func, -1)[0]  # Use -1 as the initial guess


# Test the function
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

The above code uses the `fsolve` function from `scipy.optimize` to find the root of the polynomial. This function takes a function and an initial guess as input and returns the root of the function. In this case, we define a function `func` that takes `x` as input and returns the value of the polynomial at `x`. The initial guess is set to `-1`, which is a reasonable choice for most polynomials.