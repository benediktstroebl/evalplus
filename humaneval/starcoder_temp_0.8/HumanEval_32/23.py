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

    # assert len(xs) is even number and coefficient with the largest absolute value is also non zero
    assert (
        len(xs) % 2 == 0 and abs(max(xs, key=abs)) > 0
    ), "List xs should have even length and have non zero largest coefficient"

    # points in interval will be of form (a, b) with x in (a, b)
    points = [(xs[0], xs[len(xs) - 1])]

    for _ in range(len(xs) - 1):
        next_points = []
        for point in points:
            # for every point find its local extremum
            next_points.append((point[0], point[1] / 2))
            next_points.append((point[0] / 2, point[1]))
        points = next_points

    # last point on local extremum curve is the actual solution
    return points[-1][0]

