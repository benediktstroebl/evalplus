

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

    # polynomial has to be non constant and have even degree.
    if len(xs) < 3:
        raise ValueError("xs has to have length >= 3")
    if len(xs) % 2 == 1:
        raise ValueError("xs has to have even length")

    # polynomial has to be of even degree and non constant.
    if xs[0] == 0:
        return find_zero(xs[1:])
    # polynomial is constant, so return any number.
    if len(xs) == 1:
        return 1

    # find the root of a polynomial.
    # for more info: https://en.wikipedia.org/wiki/Sturm%27s_theorem
    # this function actually uses 1 iteration of sturm sequence.
    # for n iterations:
    # def sturm(xs):
    #     curr = [xs]
    #     while len(curr[-1]) > 1:
    #         curr.append(derivative(curr[-1]))
    #         curr.extend([diffs(curr[-2], curr[-1])])
    #     return curr
    #
    # sturm_seq = sturm(xs)
    # def find_zero(sturm_seq):
    #     lo, hi = -1, 1
    #     for i in range(len(sturm_seq) - 2, 1, -2):
    #         num_sign_changes = 0
    #         for j in range(len(sturm_seq[i]) - 1):
    #             a, b = sturm_seq[i][j], sturm_seq[i][j + 1]
    #             if a * b < 0:
    #                 num_sign_changes += 1
    #                 # solve quadratic eqn to find better estimate of root.
    #                 # for more info:
    #                 # https://en.wikipedia.org/wiki/Quadratic_equation#Quadratic_formula_and_its_derivation
    #                 lo = max(lo, (a * b - math.pow(b, 2)) / (a - b))
