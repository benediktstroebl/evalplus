

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    ys = [0]
    for x in xs:
        ys.append(x)
    return ys

print(derivative([1, 2, 3]))
print(derivative([3, 1, 2, 4, 5]))