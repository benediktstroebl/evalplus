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
    # if len(xs) % 2 != 0:
    #	raise ValueError("len(xs) must be even")
    n = len(xs)
    found = False
    if n == 0:
        raise ValueError("len(xs) must be > 0")
    if n == 1:
        if xs[0] == 0:
            return xs[0]
        else:
            raise ValueError("len(xs) must be > 1")
    else:
        # the largest number non zero coefficient among the xs
        maxCoeff = max(xs)
        if maxCoeff == 0:
            raise ValueError("all coefficients are zero. Find the roots instead of find the zero.")
        # iterate all the points.
        # x = -1, x1 = 1, x2 = 1, x3 = 1, ... , x_n+1 = 1
        for i in range(n):
            point = -1
            if xs[i] != 0:
                point = -1.0 / xs[i]
            else:
                prev = poly(xs[:i], point)
                curr = poly(xs[:i + 1], point)
                if curr == 0:
                    continue
                else:
                    prev *= -1
                    point = math.sqrt(prev * prev - curr)
            degree = len(xs[:i])
            temp = poly(xs[:i + 1], point)
            if temp == 0:
                continue
            else:
                if found is False:
                    found = True
                    # the current point is the root, i.e. x = point
                    # store the degree of the polynomial
                    degree = len(xs[:i])
                    # l is the lower and u is the upper
                    l = []
                    u = []
                else:
                    # the previous point is the root
                    # replace the degree of the polynomial
                    l[degree] = point
                    u[degree] = point
        if found is False:
            raise ValueError("no roots exist. Try another x.")
        else:
            # if we have found the root for all the xs,
