

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    res = []
    if len(xs) == 1:
        return res
    elif len(xs) == 2:
        res.append(0)
        return res
    else:
        for i in range(len(xs)):
            if i == 0:
                res.append(xs[i + 1])
                continue
            elif i == 1:
                res.append(xs[i] * 2)
                continue
            else:
                res.append(xs[i] * (i + 1))
                continue
        return res

