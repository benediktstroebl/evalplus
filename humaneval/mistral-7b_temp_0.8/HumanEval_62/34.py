

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    def add(xs, ys):
        zs = [x + y for x, y in zip(xs, ys)]
        return zs

    def subtract(xs, ys):
        zs = [x - y for x, y in zip(xs, ys)]
        return zs

    def multiply(xs, ys):
        zs = [sum(p * q for p, q in zip(x, y)) for x, y in zip(xs, ys)]
        return zs

    if len(xs) == 1:
        return [0]
    if len(xs) == 2:
        return [xs[1]]
    xs = xs[:-1] + [0]
    ys = [0, 1]
    return add(multiply(xs, ys), subtract(xs, [0]))


