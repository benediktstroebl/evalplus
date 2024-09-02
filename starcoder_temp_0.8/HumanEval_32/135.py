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
    def aux(xs, prev_x):
        if len(xs) == 3:
            # if we have only three coefficients
            # use a quadratic formula
            delta = math.sqrt((xs[1] ** 2) - (4 * xs[0] * xs[2]))
            x = (-xs[1] + delta) / (2 * xs[0])
            if x == prev_x:
                # if two points are the same, find the next
                x = (-xs[1] - delta) / (2 * xs[0])
            return x
        else:
            # recursively divide and conquer
            middle = len(xs) // 2
            a = aux(xs[:middle], prev_x)
            b = aux(xs[middle:], prev_x)
            # find the zero point of a sub-problem
            if prev_x == a or prev_x == b:
                # if two points are the same, find the next
                return aux(xs[middle:], prev_x)
            elif a > b:
                # sort the sub-problem
                xs = xs[middle:]
                xs.reverse()
                return aux(xs, a)
            else:
                return aux(xs[:middle], b)
    xs.reverse()
    return aux(xs, float("inf"))
