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
    find_zero find x that makes poly(x) = 0
    find_zero returns only zero point, even if there are many.
    check test - is used to verify if x is a root of polynomial or not.
    if largest non zero coefficient is negative:
        x = -1/abs(xs[0]) * (-1)**(len(xs) - 1)
        # do other things
    if all(abs(x) < 1):
        return x
    # do other things
    return None


# Example usage
xs = [1, 2]
x = find_zero(xs)
print("The root of polynomial is: ", x)
```