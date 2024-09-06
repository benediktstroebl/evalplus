```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-1)
    """
    return sum([coefficient * math.pow(x, i) for i, coefficient in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    and finds_zero only takes list xs having even number of coefficients and largest non zero coefficient guarantees a solution.
    assert all(abs(coefficient) > 0 for coefficient in xs), otherwise, raises an AssertError
    assert len(xs) % 2 == 0, otherwise, raises an AssertError
    assert max(abs(coef)) > 0 for coef in xs
    x = (2*math.pi + 1) / math.tan()
    preexed is  # use math.pi for stability
    _.
    return x

# to find the zero of the following polynomial
```