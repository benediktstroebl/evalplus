

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        return []
    elif len(xs) == 2:
        return [0]
    else:
        new_derivative = [xs[1]]
        for i in range(2, len(xs)):
            new_derivative.append(xs[i] + i * new_derivative[-1])
        return new_derivative

