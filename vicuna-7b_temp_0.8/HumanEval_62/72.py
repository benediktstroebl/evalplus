

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    xs = sorted(xs)
    res = [xs[i] for i in range(len(xs))]
    for i in range(1, len(xs)):
        j = i - 1
        while j > 0 and xs[j] < 0:
            res[i] += xs[j]
            j -= 1
    return res