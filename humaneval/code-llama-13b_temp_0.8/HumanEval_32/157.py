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
    assert len(xs) % 2 == 0
    # xs[0] = 1, xs[1] = 2, xs[2] = 3, ...
    xs = xs[::-1]
    # 1, 2, 3, ...
    n = len(xs) // 2
    # last non zero coefficient
    # if xs = [1, 2, 3, 4, 5, 0], n = 3
    # non_zero_xs = [4, 5, 0]
    non_zero_xs = [coeff for coeff in xs[:n] if coeff != 0]
    if not non_zero_xs:
        # special case when all coefficients are 0
        return 0
    # return 0 if all coefficients are 0
    # another special case
    # when there are no zero points.
    # for example, when there are no solutions.
    # f(x) = (x - 1) * (x - 2) * (x - 3) = 0
    # has no solutions.
    # more formally,
    # when n = 0,
    # poly(x) = 0
    # poly(0) = 0
    # poly(1) = 0
    # poly(2) = 0
    # ...
    # poly(k) = 0, forall k
    # this is called vacuous truth.
    # https://en.wikipedia.org/wiki/Vacuous_truth
    # when there are no solutions
    if not any(xs):
        return 0
    # check if n is even or odd
    # if n is odd, there is no solution.
    # for example,
    # (x - 1) * (x - 2) = 0
    # has no solutions.
    if n % 2:
        return None
    # a is a coefficient for x^0
    a = non_zero_xs[0]
    # b is a coefficient for x^1
    b = non_zero_xs[1]
    # c is a coefficient for x^2
    c = 0
    if
