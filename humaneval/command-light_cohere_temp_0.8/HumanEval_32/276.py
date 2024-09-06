```python
import math
def evaluate_polynomial(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])
def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that the polynomial is zero, returns only zero point, even if there are many solutions.
    """
    first, ensure that xs has even number of coefficients, and the largest non-zero coefficient is guaranteed a solution. The function uses binary search to find this solution, which is the correct approach and guarantees no duplicates.
    """
    value of x, is checked by comparing it with the last coefficient's x-related term, starting from the highest degree term (xs[-1] * x**(-1)) and moving downwards by decreasing the degree of the term.
    high = float(find_zero([1, 2]))  # f(x) = 1 + 2x -0.5
    low = float(find_zero([-6, 11, -6, 1]))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    print(f'largest solution: x = {low:.2f}, y = {high:.2f}'))
```