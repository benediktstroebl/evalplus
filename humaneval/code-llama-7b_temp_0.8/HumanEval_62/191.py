

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # base case: 0, 1, 2
    # 0:
    if len(xs) == 0:
        return []

    # 1:
    if len(xs) == 1:
        return []

    # 2:
    if len(xs) == 2:
        return [xs[1]]

    # 3:
    if len(xs) == 3:
        return [xs[1], 2 * xs[2]]

    # 4:
    if len(xs) == 4:
        return [xs[1], 2 * xs[2], 3 * xs[3]]

    # 5:
    if len(xs) == 5:
        return [xs[1], 2 * xs[2], 3 * xs[3], 4 * xs[4]]

    # 6:
    if len(xs) == 6:
        return [xs[1], 2 * xs[2], 3 * xs[3], 4 * xs[4], 5 * xs[5]]

    # 7:
    if len(xs) == 7:
        return [xs[1], 2 * xs[2], 3 * xs[3], 4 * xs[4], 5 * xs[5], 6 * xs[6]]

    # 8:
    if len(xs) == 8:
        return [xs[1], 2 * xs[2], 3 * xs[3], 4 * xs[4], 5 * xs[5], 6 * xs[6], 7 * xs[7]]

    # 9:
    if len(xs) == 9:
        return [xs[1], 2 * xs[2], 3 * xs[3], 4 * xs[4], 5 * xs[5], 6 * xs[6], 7 * xs[7], 8 * xs[8]]

    # 10:
    if len(xs) == 10:
        return [xs[1], 2 * xs[2], 3 * xs[3], 4 * xs[4], 5 *
