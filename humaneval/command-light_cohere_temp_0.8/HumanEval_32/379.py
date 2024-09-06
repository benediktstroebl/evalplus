```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0, x is in the domain of x, and x is not a root of any polynomial in the given list.
    if len(xs) != 2 or not all(xs[i] > 0 for i in range(len(xs))) or xs[0] + xs[1] * x + xs[1] * x^2 + ...):
        return None  # invalid input

    # special case: seive quadratic
    if len(xs) == 2 and xs[0] * xs[1] == 0:
        return math.sqrt(xs[0])

    # find root of polynomial using Newton's method
    ans = 0
    for i in range(len(xs)):
        # store x value in ans
        ans += xs[i] * (xs[i] - ans) / (xs[i] - ans) ** 2
    return ans


# test cases
print(find_zero([1, 2])) # f(x) = 1 + 2x
-0.5 # root is +2 -
print(find_zero([-6, 11, -6, 1])) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
1.5 # root
0
```