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

    low, high = min(xs), max(xs)
    if low == 0:
        return 0.0
    if high == 0:
        return float('inf')
    if len(xs) == 2 and high == low:
        return 0.0 if xs[0] > 0 else -xs[0]
    # [a, b] -> [a, a + b]
    xs = [x if x!= 0 else low + high for x in xs]
    # monotone increase
    if all(xs[i] <= xs[i+1] for i in range(len(xs) - 1)):
        return float('nan')
    # [a, b] -> [a, a - b]
    xs = [x if x!= high else low - high for x in xs]
    # [a, b] -> [a + b, b]
    xs = [2 * xs[-1] - xs[-2]] + xs[:-2]
    # [a, b, c, d] -> [a, b, c + d, d
