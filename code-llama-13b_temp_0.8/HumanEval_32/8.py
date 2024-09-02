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

    def bisect(low: float, high: float):
        """
        Returns mid point of high and low if low and high are different.
        Otherwise returns None
        """
        return None if low == high else (low + high) / 2

    def bi_search(low: float, high: float, func, epsilon):
        """
        Applies binary search to find x such that func(x) = 0.
        It is assumed that low and high are roots
        """
        mid = bisect(low, high)
        if mid is None:
            return low
        elif func(low) * func(mid) < 0:
            return bi_search(low, mid, func, epsilon)
        else:
            return bi_search(mid, high, func, epsilon)

    func = lambda x: poly(xs, x)
    low = -1.0
    high = 1.0
    # Get lower bound
    while not func(low) <= 0 <= func(high):
        low *= 2
        high *= 2

    return bi_search(low, high, func, 1e-10)

