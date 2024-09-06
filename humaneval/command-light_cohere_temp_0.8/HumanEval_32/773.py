```python
import math
def poly(xs: list, x: float) -> int:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    and returns only zero point, even if there are many.
    find_zero takes list xs having even number of coefficients and largest non-zero coefficient guarantees a solution.
    return round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    return round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    ```
The code defines two functions: `poly` and `find_zero`. The `poly` function computes the value of a polynomial with a list of coefficients at a given point. The `find_zero` function finds the zero of a polynomial with a list of coefficients. 

The `find_zero` function returns the zero of the polynomial, which is the only zero point of the polynomial. The `poly` function returns the function by summing the products of the coefficients of the polynomial evaluated at the given point. The `find_zero` function returns the zero of the polynomial, which is the only zero point of the polynomial.