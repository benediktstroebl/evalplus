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
    if len(xs) < 2:
        return 0
    n = len(xs) - 1
    # Find out number of terms in a factor.
    for i in range(2, n + 1):
        if n % i == 0:
            n = i
            break
    # Now n is factor.
    l = math.floor(n / 2)
    left = 0
    right = 1000
    epsilon = 0.0001
    while left < right:
        mid = (left + right) / 2
        if abs(poly(xs, mid)) < epsilon:
            return mid
        if poly(xs, mid) > 0:
            right = mid
        else:
            left = mid
    return mid

