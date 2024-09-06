```python
import math
def evaluate_polynomial(xs):
    """
    Evaluates polynomial with coefficients xs at point x, returns sum of coefficients multiplied by x^n.
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes polynomial(x) = 0, returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    return:
        >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
        -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
        1.0
    """
   
    return None
"""

test_functions = {
    "evaluate_polynomial": [("xs", evaluate_polynomial)],
    "find_zero": [("xs", find_zero)]
}

# Test
print(test_functions)
```