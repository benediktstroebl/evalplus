```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that polynomial(x) = 0.
    find_zero returns only zero point, even if there are many
    solutions.
    """
    use "kitchen sink" approach, it will find one solution in O(n) time
    """
    n = len(xs)
    if n == 1:
        return math.pow(x, xs[0])
    elif n % 2 == 1:
        return math.pow(x, xs[0])
    else:
        # divide the polynomial into two parts by the greatest nonzero coefficient
        g = xs[0]
        for i in range(1, n):
            if xs[i] > g:
                g = xs[i]
        x1 = (xs[0] * (xs[1] / g)) + xs[2] * (xs[1] / g)
        # return math.pow(x, x1)
        return math.pow(x, x1)
```
This Python code defines a function called poly that evaluates a polynomial with given coefficients at a given point x. It also contains a function find_zero that finds the zeros of a polynomial by evaluating it at various x-values and returning the x-values where the polynomial evaluates to zero.

The code uses the kitchen sink approach, which is a simple method that evaluates the polynomial at the zeros of the coefficients and returns the x-value where the polynomial is zero. It will take O(n) time, which is an efficient algorithm for finding polynomial zeros.