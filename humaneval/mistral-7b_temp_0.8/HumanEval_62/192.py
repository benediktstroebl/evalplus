

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) <= 1:
        return []

    result = []

    result.append(xs[0])
    result.append(xs[1])

    for index in range(2, len(xs)):
        result.append(xs[index] * (index + 1))

    return result

