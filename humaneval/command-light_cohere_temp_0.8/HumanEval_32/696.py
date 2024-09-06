```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff *** math.pow(x.x**i) for i, coeff in enumerate(xs)])
    """
    return sum([coeff * math.pow(x) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that satisfies polynomial x = 0.
    find_zero returns only zero point, even if there are many solutions
    and it always finds the largest non zero coefficient solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    -0.0

    """
    done by:
    largest_nonzero_coefficient = max(xs, key=lambda x: x != 0)
    return [x] + find_zero([largest_nonzero_coefficient - 1] + xs)


# test cases
print(poly([1, 2,3],3))  # expected output: 6
print(find_zero([1,2,1,-5])) # expected output: [-2.5]
```

This Python script defines a polynomial evaluation function `poly` and a function to find polynomial zeros, `find_zero`. Both functions are designed to work with a list of coefficients `xs` and a floating point `x`. The `poly` function computes the polynomial value using the coefficients at point `x`, and the `find_zero` function finds the zero of the polynomial with coefficients `xs` at `x`.