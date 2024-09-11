### Polynomial Evaluation and Zero Finding
```python
import math

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
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    n = len(xs) - 1
    try:
        x = -xs[-1] / (2 * xs[-2])
        return round(x, 2)
    except ZeroDivisionError:
        # If even number of coefficients but no quadratic term,
        # we have to find roots (x - r1)(x - r2) = 0, i.e. x^2 - (r1 + r2)x + r1*r2 = 0
        if xs[-2] == 0:
            a = 1
            b = -xs[-1]/xs[-3]
            c = xs[-1]*xs[-2]/xs[-3]
            return round((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a), 2), round((-b - math.sqrt(b**2 - 4*a*c)) / (2 * a), 2)
        else:
            return "This polynomial has no solution."

# Test cases
print(find_zero([1, 2])) # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1])) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```
Note that for polynomials with an even number of coefficients but no quadratic term (i.e., polynomials that are products of two or more linear factors), we need to use a different method to find the roots, which is the quadratic formula for the product of two linear factors. The script handles this case by attempting to divide the coefficients of the polynomial by the coefficients of its quadratic term and applying the quadratic formula. If this fails (i.e., a ZeroDivisionError is raised), the script assumes that the polynomial has no solution.