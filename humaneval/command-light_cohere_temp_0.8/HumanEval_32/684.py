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
    find_zero find x such that poly(x) = 0
    find_zero returns x, or a ValueError if no solutions.
    """
    using back or testing a polynomial with real coefficients.
    use x = 0.0 to find using using the determined by finding the largest nonzero coefficient and plugging it into x = coeff / x**n
    """
    return x

# Example usage
xs = [1, 2]
x = find_zero(xs)
print(x)
```