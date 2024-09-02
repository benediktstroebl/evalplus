import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 == 0:
        return float("nan")
    if xs[0] != 0:
        return float("nan")
    xs = [-coeff for coeff in xs[1:]]
    xs.append(0)
    # store in stack.
    # stack has initial value x = 1,  f(1) is greater than 0.
    stack = [(0.0, 1.0)]
    x = stack[-1]
    f = poly(xs, x)
    while f > 0:
        # if f(x) > 0, then x = x/2.
        # if f(x) < 0, then x = x + (f(x) / f'(x))
        x = x / 2.0
        f = poly(xs, x)
        stack.append((x, f))
    # iteratively find a zero point using bisection.
    # return stack[-1][0]
    while len(stack) > 1:
        x0, f0 = stack.pop()
        x1, f1 = stack[-1]
        x = (x0 + x1) / 2.0
        f = poly(xs, x)
        if f * f0 > 0:
            stack.append((x0, f0))
        else:
            stack.append((x, f))
    return stack[-1][0]

