```python
import math
def evaluate_polynomial(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    """
    return sum([coef * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that polynomial (xs) = 0, returns only zero point, even if there are many roots.
    moreover, find_zero only takes list xs having even number of coefficients and largest non-zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   
    standardise a root-finding algorithm, but it's more efficient.
    """
    return math.ldn x x in xs[0]

def test(xs):
    """
    Test if a list of coefficients satisfies the polynomial equation
    """
    evaluate_polynomial(xs, x) == 0

# Example usage
xs = [1, 2]
test(xs)  # True
xs = [-6, 11, -6, 1]
test(xs)  # False
```