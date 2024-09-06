```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    and it finds the unique solution by avoiding non-zero coefficients
    """
    if len(xs) != 2:
        raise ValueError("find_zero requires list with at least two coefficients")
    m, b = xs[0], xs[1]
    while True:
        x = (b**2 + 4*m*b + 4*m**2*x - 4*xs[0]*x) // (2*b - 4*xs[0])
        if x == 0:
            return x
    return None

# Test cases
test_cases = [
    [(-3, -4), (-1, 1)],
    [(1, 0)],
    [(-1, -5), (2, 3)],
    (2, 1),
    (2, -1),
    (-6, 11), (-6, -10),
    (6, -6),
    (3, -3), (5, -2),
    (-1, -1), (4, -4),
]

# Calculate results
for case in test_cases:
    result = find_zero(case)
    if result is not None:
        print(f"x = {result}")
```