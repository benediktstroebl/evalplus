

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 0:
        raise ValueError
    if len(xs) == 1:
        return []

    # Handles edge case
    if len(xs) == 2:
        return [xs[1] * 1]
    # Main function
    # xs[0] + xs[1] * x + xs[2] * x^2 + ....
    # f` = (0 * 0) + (0 * 1) + (1 * 2) * x + (2 * 3) * x^2 + ....
    # [1, 2, 3, 4, 5, ....]
    # [0, 0, 1, 2, 3, ....]
    #
    ys = []
    ys.append(0)
    for i in range(1, len(xs)):
        ys.append(i * xs[i])
    return ys[1:]

