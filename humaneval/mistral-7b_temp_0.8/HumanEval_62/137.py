

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    new_xs = []
    if len(xs) == 0:
        return new_xs
    elif len(xs) == 1:
        return [xs[0]]
    else:
        for i in range(1, len(xs)):
            if i == 1:
                new_xs.append(xs[i] * i)
            else:
                new_xs.append(xs[i] * i)
                new_xs.append(0)
        return new_xs

