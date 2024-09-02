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
    if len(xs) % 2 == 1 or xs[-1] == 0:
        raise ValueError("invalid argument")
    # see https://en.wikipedia.org/wiki/Sturm%27s_theorem
    a = xs[-1]
    b = poly(xs[:-1], 0)
    p = [a, b]
    n = len(p)
    # d = [-p[n - 1], -p[n - 2]]
    d = [-(p[n - 1]), -(p[n - 2])]
    m = 2
    while abs(d[m - 1]) > 1e-10:
        # 1. compute d coefficients.
        c = poly(d, 0)
        d = [c, -(a * c - b)]
        m += 1
        # 2. compute p coefficients.
        b = poly(p, m)
        a = b
        p = [a] + p
        p = p[:m + 1]

    # print(d)
    # 3. find p_m such that p_m = 0
    # 3.1 find m_1.
    # d[0] - d[1]
    m1 = 0
    while d[m1] > 0:
        m1 += 1
    # 3.2 find m_2
    m2 = m1
    while d[m2] < 0:
        m2 += 1
    # 3.3 find m
    # 3.3.1
    m = min(m1, m2)
    # 3.3.2
    x1 = find_zero_from_d(d[m1], d[m1 - 1], p[m1], p[m1 - 1])
    x2 = find_zero_from_d(d[m2], d[m2 - 1], p[m2], p[m2 - 1])
    # 3.3.3
    m = m1 if abs(x2 - x1) < 1e-10 else m2

