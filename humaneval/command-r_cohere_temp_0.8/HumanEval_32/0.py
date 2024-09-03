```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero point of a polynomial with given coefficients xs.
    The function returns one zero point, even if there are multiple ones.
    It's guaranteed to work if xs has even number of elements and
    the highest non-zero coefficient.
    """
    # Ensure the highest non-zero coefficient is at the end
    non_zero_idx = next((i for i, x in enumerate(xs) if x != 0), len(xs))
    xs = xs[non_zero_idx:] + xs[:non_zero_idx]

    # Use the fact that polynomial has x=0 as a root
    # and use backward substitution
    x_n = 1 / math.pow(xs[-1], -1)
    for i in range(len(xs) - 1, 0, -1):
        x_i = x_n * (-xs[i] / xs[i + 1])
        x_n = x_i + math.pow(x_i, len(xs) - i - 1)
    return x_i
```