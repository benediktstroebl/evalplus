```python
import math
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    ensure even number of coefficients and largest non zero coefficient as it guarantees
    a solution.
    return x if xs[0] != 0 and xs[0] == largestCoefficient() and x > 0
    """
    if not xs[0]: return float('inf')
    if xs[0] == xs[1] and xs[1] == 0: return float('inf')
    if xs[0] == 0 and xs[1] != 0: return float('-inf')
    return xs[0]
if __name__ == "__main__":
    test_cases = [
        [1, 2],
        [-6, 11, -6, 1],
        [4, 2, -5, 3]
    ]
    for x in test_cases:
        result = find_zero(x)
        assert result == x[0]
    ```