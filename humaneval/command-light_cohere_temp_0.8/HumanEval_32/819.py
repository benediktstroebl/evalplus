```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    assert all(x != 0 for x in [x for x in range(1) if x not in xs]),
    assert all(x != 1 for x in [x for x in range(1) if x not in xs]),
    assert xs[0] == 0, "Largest non zero coefficient is not 0"
    assert xs[-1] == 1, "Smallest non zero coefficient is not 1"
    assert xs[0] == xs[-1], "even number of coefficients"
    assert max(abs(x - xs[0])) < 1e-6, "Distance between zero and largest non zero coefficient is too big"
    assert all(x == xs[0]) or all(x == xs[-1]) or all(x == xs[i] for i in range(1, len(xs)-2)),
    assert all([x == xs[i] for i in range(1, len(xs)) for x in xs]),
    assert all([x in xs[1:]] for x in range(1, len(xs))),
    assert all([x in xs[1:-1]] for x in range(1, len(xs))),
    assert all([x == xs[i] for i in range(2, len(xs)) for x in xs]) or all(x == xs[i] for i in range(2, len(xs)-2)),
    return [xs[0]]

poly([1, 2], x) # 0
find_zero([1, 2]) # [0]
``` 
Do you have any questions about the code?