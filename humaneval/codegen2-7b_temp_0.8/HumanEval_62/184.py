

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    x_index = 0
    y = xs[x_index]
    result = [xs[x_index + 1]]
    while x_index < len(xs) - 1:
        x_index += 1
        y += xs[x_index]
        result.append(y)
    return
