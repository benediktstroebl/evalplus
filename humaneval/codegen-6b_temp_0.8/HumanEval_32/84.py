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
    def find_one_solution(a: list):
        """
        Only one solution can be found, as it guarantees a solution.
        """
        c0 = a[0]
        for i in range(1, len(a)):
            c0 = (c0 - a[i]) / a[i]
        return -c0 / a[0]

    if len(xs) % 2 != 0 or not max(abs(x) for x in xs):
        raise ValueError('find_zero takes list of coeffs having even number of coeffs and Largest non zero coeff as it guarantees a solution')
    negative = False
    for i in range(1, len(xs)):
        if xs[i] * xs[i - 1] < 0:
            negative = True
    if negative:
        xs = [x for x in xs]
        for i in range(1, len(xs)):
            xs[i] = -xs[i]
        return find_one_solution(xs)
    else:
        return find_one_solution(xs)

