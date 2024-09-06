

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    ret_val = []
    for index in range(len(xs)):
        if index == 0:
            ret_val.append(0)
        elif index == 1:
            ret_val.append(xs[0])
        else:
            ret_val.append(ret_val[index - 1] * (index - 1) + xs[index])

    return ret_val

