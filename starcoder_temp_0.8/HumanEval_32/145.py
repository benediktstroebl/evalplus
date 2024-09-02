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
    if len(xs) % 2!= 0:
        raise ValueError("coefficient list length must be even")

    for i, coeff in enumerate(xs):
        if coeff!= 0:
            break

    d = len(xs) // 2
    p = xs[i: i+d]
    q = xs[-d:]

    u = [1] + [0] * d
    v = [0] + [1] * d
    while d >= 2:
        if i % 2 == 0:
            q_u = q[0] * u[0] + sum(q[j] * u[j] for j in range(1, d))
            u = [q_u] + [0] * (d-1)
            p_v = p[0] * v[0] + sum(p[j] * v[j] for j in range(1, d))
            v = [p_v] + [0] * (d-1)
        else:
            p_u = p[0] * u[0] + sum(p[j] * u[j] for j in range(1, d))
            u = [p_u] + [0] * (d-1)
            q_v = q[0] * v[0] + sum(q[j] * v[j] for j in range(1, d))
            v = [q_v] + [0] * (d-1)

        d = d // 2
        i = i // 2

    if i % 2 == 0:
        return u[0] / v[0]
    else:
        return -u[0] / v[0]

