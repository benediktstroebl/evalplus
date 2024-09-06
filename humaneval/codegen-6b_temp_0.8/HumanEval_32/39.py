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
    n = len(xs)
    if n % 2:
        raise ValueError("x should be a list of even number of elements")
    largest_coeff = max(xs, key=abs)
    if largest_coeff == 0:
        raise ValueError("a polynomial with non-zero coefficient should always have non-zero roots")
    xs_without_largest_coeff = [x for x in xs if abs(x) != abs(largest_coeff)]
    candidate_xs = [(1, x) for x in xs_without_largest_coeff]
    for i, coeff in enumerate(xs):
        for x, _ in candidate_xs:
            if x ** (n // 2) == coeff:
                mid_point = x
        for j, x in enumerate(xs):
            if i != j:
                candidate_xs.append((-1 * x / mid_point, x))
    for x, _ in candidate_xs:
        if abs(poly(xs, x)) < 1E-5:
            return x
    raise ValueError("No such value of x satisfies the polynomial with given coefficients")

