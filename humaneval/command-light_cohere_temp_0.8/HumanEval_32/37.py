```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x that makes polynomial equal to 0.
    find_zero returns only zero point, even if there are many solutions
    """
    if len(xs) % 2 != 0:
        raise ValueError("List of coefficients must have even length.")

    # Sort coefficients in descending order
    xs.sort(xs, reverse=True)
    # Find root of the determinant of the coefficient matrix
    determinant = math.sqrt(abs(x[0]) * xs[0] - xs[1] * x[0])
    for x_root in range(-determin, abs(determin)):
        if determinant == 0:
            break
        determinant = determinant * x_root
    return x_root

xs = [1, 2]
x = find_zero(xs)
print(f"The solution is {x}")

```